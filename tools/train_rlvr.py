#!/usr/bin/env python3
"""Reinforcement on task feedback, not imitation of reference solutions.

The six earlier weight routes all trained the model to resemble answers. This one trains it to pass
the hidden tests: sample several solutions per task, score them with the executable tests, and push
the policy toward the ones that pass using a group-relative advantage (the GRPO form). Nothing here
sees a reference solution.

  python3 tools/train_rlvr.py --out /home/vault/work/rlvr-1.5b --tasks 60 --samples 4
"""
import argparse
import json
import random
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import torch
import torch.nn.functional as F
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

ROOT = Path(__file__).resolve().parent.parent
SPLIT_FROM = 120          # tasks 0-119 are evaluation; never used here
MAX_NEW = 320


FAMILY = ROOT / "families" / "mbpp-basics" / "family.json"


def task_rows(n, seed=0):
    """Training tasks come from the family itself, so each one carries its own test file."""
    fam = json.loads(FAMILY.read_text())
    pool = fam["tasks"][SPLIT_FROM:]
    random.Random(seed).shuffle(pool)
    return pool[:n]


def prompt_for(tok, t):
    msgs = [{"role": "user", "content": "Task: %s\n\nReturn only Python code in one fenced block. "
                                       "Define exactly the function named %s."
                                       % (t["spec"].strip(), t.get("entry") or "")}]
    return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)


def extract(text):
    """Pulling code out of a completion that may be truncated before its closing fence."""
    m = re.search(r"```(?:python)?\s*\n(.*?)(?:```|$)", text, re.S)
    body = m.group(1) if m else text
    body = re.sub(r"^\s*```[a-zA-Z]*\s*", "", body)
    return (body.strip() + "\n")


def passes(code, t):
    tf = ROOT / "families" / "mbpp-basics" / t["tests"]
    if not tf.exists():
        return None
    with tempfile.TemporaryDirectory(prefix="rl-") as td:
        p = Path(td)
        (p / "solution.py").write_text(code)
        (p / Path(tf).name).write_text(tf.read_text())
        try:
            r = subprocess.run([sys.executable, str(p / tf.name)], cwd=td,
                               capture_output=True, text=True, timeout=20)
            return r.returncode == 0
        except subprocess.TimeoutExpired:
            return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen2.5-Coder-1.5B-Instruct")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tasks", type=int, default=60)
    ap.add_argument("--samples", type=int, default=4)
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--max-new", type=int, default=MAX_NEW)
    a = ap.parse_args()

    tok = AutoTokenizer.from_pretrained(a.model)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.float16,
                             bnb_4bit_use_double_quant=True)
    model = AutoModelForCausalLM.from_pretrained(a.model, quantization_config=bnb,
                                                 device_map={"": 0}, torch_dtype=torch.float16)
    model = prepare_model_for_kbit_training(model)
    cfg = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.0, bias="none", task_type="CAUSAL_LM",
                     target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])
    model = get_peft_model(model, cfg)
    model.print_trainable_parameters()
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=a.lr)

    rows = task_rows(a.tasks)
    print("tasks %d, samples %d, epochs %d" % (len(rows), a.samples, a.epochs), flush=True)
    stats = {"tasks": 0, "skipped_flat": 0, "solved_any": 0, "solved_all": 0, "steps": 0}
    t0 = time.time()
    for ep in range(a.epochs):
        for t in rows:
            stats["tasks"] += 1
            text = prompt_for(tok, t)
            ids = tok(text, return_tensors="pt", truncation=True, max_length=512).to(model.device)
            with torch.no_grad():
                out = model.generate(**ids, max_new_tokens=a.max_new, do_sample=True,
                                     temperature=0.9, top_p=0.95, num_return_sequences=a.samples,
                                     pad_token_id=tok.eos_token_id)
            comp = out[:, ids["input_ids"].shape[1]:]
            rewards = []
            for j in range(a.samples):
                code = extract(tok.decode(comp[j], skip_special_tokens=True))
                ok = passes(code, t)
                rewards.append(0.0 if ok is None else float(ok))
            n_ok = sum(rewards)
            if n_ok == 0:
                stats["skipped_flat"] += 1
                continue
            stats["solved_any"] += 1
            stats["solved_all"] += int(n_ok == a.samples)
            rw = torch.tensor(rewards, device=model.device)
            adv = rw - rw.mean()
            if adv.std() == 0 or adv.abs().sum() == 0:
                stats["skipped_flat"] += 1
                continue
            adv = adv / (rw.std() + 1e-4)
            # log-probability of each sampled completion under the current policy
            full = torch.cat([ids["input_ids"].repeat(a.samples, 1), comp], dim=1)
            logits = model(input_ids=full).logits[:, :-1]
            logp = F.log_softmax(logits.float(), dim=-1)
            tgt = full[:, 1:]
            lp = logp.gather(-1, tgt.unsqueeze(-1)).squeeze(-1)
            lp = lp[:, ids["input_ids"].shape[1] - 1:]
            loss = -(adv.unsqueeze(1) * lp).sum() / max(lp.numel(), 1)
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_([p for p in model.parameters() if p.requires_grad], 1.0)
            opt.step()
            stats["steps"] += 1
            if stats["steps"] % 5 == 0:
                print("ep %d task %d: rewards %s loss %.4f elapsed %.1f min"
                      % (ep, stats["tasks"], rewards, float(loss), (time.time() - t0) / 60), flush=True)
            del logits, logp, lp, loss, full, comp, out
            torch.cuda.empty_cache()

    model.save_pretrained(a.out)
    tok.save_pretrained(a.out)
    stats["minutes"] = round((time.time() - t0) / 60, 1)
    Path(a.out).mkdir(parents=True, exist_ok=True)
    (Path(a.out) / "rlvr-stats.json").write_text(json.dumps(stats, indent=1) + "\n")
    print(json.dumps(stats, indent=1), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
