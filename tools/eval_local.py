#!/usr/bin/env python3
"""Evaluate a local model, with and without the LoRA adapter, on held-out MBPP tasks.

Same tests, same scoring, same refusal as every other run in this repo. No API calls.

  python3 tools/eval_local.py --family families/mbpp-test60 --out runs/weights-mbpp-test60.json
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL = "Qwen/Qwen2.5-Coder-0.5B-Instruct"
ROOT = Path(__file__).resolve().parent.parent


def load(model_path=None):
    tok = AutoTokenizer.from_pretrained(MODEL)
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.float16,
                             bnb_4bit_use_double_quant=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL, quantization_config=bnb,
                                                 device_map={"": 0}, torch_dtype=torch.float16)
    if model_path:
        model = PeftModel.from_pretrained(model, model_path)
    model.eval()
    return tok, model


def gen(tok, model, task, max_new=320):
    msgs = [{"role": "user", "content": "Task: %s\n\nReturn only Python code in one fenced block. "
                                       "Define exactly the function named %s."
                                       % (task["spec"], task.get("entry", task["id"]))}]
    text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    ids = tok(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**ids, max_new_tokens=max_new, do_sample=False,
                             pad_token_id=tok.eos_token_id)
    raw = tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True)
    m = re.search(r"```(?:python)?\s*\n(.*?)```", raw, re.S)
    return ((m.group(1) if m else raw).strip() + "\n")


def score(code, test_path, entry):
    with tempfile.TemporaryDirectory(prefix="ev-") as td:
        p = Path(td)
        (p / "solution.py").write_text(code)
        t = p / Path(test_path).name
        t.write_text(Path(test_path).read_text())
        try:
            r = subprocess.run([sys.executable, str(t)], cwd=td, capture_output=True, text=True, timeout=30)
            return r.returncode == 0
        except subprocess.TimeoutExpired:
            return False


def run_arm(name, model_path, tasks, fam_dir):
    tok, model = load(model_path)
    res = {}
    t0 = time.time()
    for i, t in enumerate(tasks, 1):
        code = gen(tok, model, t)
        ok = score(code, fam_dir / t["tests"], t.get("entry", t["id"]))
        res[t["id"]] = {"pass": ok, "code_sha256": __import__("hashlib").sha256(code.encode()).hexdigest()}
        if i % 10 == 0:
            print("%s %d/%d" % (name, i, len(tasks)), flush=True)
    passed = sum(1 for v in res.values() if v["pass"])
    print("%s: %d/%d = %.4f in %.1f min" % (name, passed, len(tasks), passed / len(tasks),
                                            (time.time() - t0) / 60), flush=True)
    del model
    torch.cuda.empty_cache()
    return {"passed": passed, "of": len(tasks), "accuracy": round(passed / len(tasks), 4), "results": res}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", default="families/mbpp-test60")
    ap.add_argument("--adapter", default="/home/vault/work/lora-mbpp")
    ap.add_argument("--out", required=True)
    ap.add_argument("--order", choices=["base-first", "tuned-first"], default="base-first",
                    help="arm order; counterbalanced across sets to expose cache warm-up bias")
    a = ap.parse_args()

    fam_dir = ROOT / a.family
    fam = json.loads((fam_dir / "family.json").read_text())
    tasks = fam["tasks"]

    if a.order == "base-first":
        base = run_arm("base", None, tasks, fam_dir)
        tuned = run_arm("tuned", a.adapter, tasks, fam_dir)
    else:
        tuned = run_arm("tuned", a.adapter, tasks, fam_dir)
        base = run_arm("base", None, tasks, fam_dir)

    up = sum(1 for t in tasks if tuned["results"][t["id"]]["pass"] and not base["results"][t["id"]]["pass"])
    down = sum(1 for t in tasks if base["results"][t["id"]]["pass"] and not tuned["results"][t["id"]]["pass"])
    report = {"kind": "weights", "date": time.strftime("%Y-%m-%d"), "model": MODEL,
              "adapter": a.adapter, "family": a.family, "order": a.order,
              "base": {k: base[k] for k in ("passed", "of", "accuracy")},
              "tuned": {k: tuned[k] for k in ("passed", "of", "accuracy")},
              "delta": round(tuned["accuracy"] - base["accuracy"], 4),
              "improved": up, "regressed": down,
              "verdict": "pass" if tuned["accuracy"] - base["accuracy"] >= 0.05 and tuned["accuracy"] >= base["accuracy"] else "fail",
              "results": {"base": base["results"], "tuned": tuned["results"]}}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("base", "tuned", "delta", "improved", "regressed", "verdict")}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
