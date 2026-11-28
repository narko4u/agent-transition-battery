#!/usr/bin/env python3
"""Weight-level transfer, free and local: LoRA on verified MBPP solutions, 4GB card.

This is the sixth M2 route and the weight-level question at the same time. No API spend, no rented
GPU, no weights of a frontier model. A 0.5B open coder model is tuned on the solved half of MBPP and
tested on tasks it has never seen, using the same executable tests as every other run in this repo.

  python3 tools/train_lora.py --out /home/vault/work/lora-mbpp
"""
import argparse
import json
import os
import time
from pathlib import Path

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig,
                          DataCollatorForLanguageModeling, Trainer, TrainingArguments)

MODEL = "Qwen/Qwen2.5-Coder-0.5B-Instruct"   # overridden by --model
SPLIT_FROM = 120          # tasks 0-119 are the evaluation zone, never trained on
MAX_LEN = 640             # overridden by --max-len


def load_rows(path="/tmp/mbpp.json"):
    rows = json.loads(Path(path).read_text())
    out = []
    for i, r in enumerate(rows):
        if i < SPLIT_FROM:
            continue
        code = (r.get("code") or "").strip()
        prompt = (r.get("prompt") or "").strip()
        entry = (r.get("entry_point") or "").strip()
        if not code or not prompt:
            continue
        if entry and ("def %s" % entry) not in code:
            continue
        out.append({"i": i, "prompt": prompt, "code": code, "entry": entry})
    return out


def build_dataset(rows, tok, max_len=MAX_LEN):
    def conv(r):
        msgs = [{"role": "user", "content": "Task: %s\n\nReturn only Python code in one fenced block. "
                                           "Define exactly the function named %s." % (r["prompt"], r["entry"])},
                {"role": "assistant", "content": "```python\n%s\n```" % r["code"]}]
        text = tok.apply_chat_template(msgs, tokenize=False)
        enc = tok(text, truncation=True, max_length=max_len, padding=False)
        prompt_only = tok.apply_chat_template(msgs[:1], tokenize=False, add_generation_prompt=True)
        n_prompt = len(tok(prompt_only, truncation=True, max_length=max_len)["input_ids"])
        labels = list(enc["input_ids"])
        for k in range(min(n_prompt, len(labels))):
            labels[k] = -100
        enc["labels"] = labels
        return enc
    return Dataset.from_list([conv(r) for r in rows])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/home/vault/work/lora-mbpp")
    ap.add_argument("--epochs", type=float, default=3.0)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--rows", default="/tmp/mbpp.json")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--max-len", type=int, default=MAX_LEN)
    ap.add_argument("--lora-r", type=int, default=16)
    a = ap.parse_args()
    model_id, max_len = a.model, a.max_len

    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    rows = load_rows(a.rows)
    print("model %s, max_len %d, rows %d (split at %d)" % (model_id, max_len, len(rows), SPLIT_FROM), flush=True)

    tok = AutoTokenizer.from_pretrained(model_id)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                             bnb_4bit_compute_dtype=torch.float16,
                             bnb_4bit_use_double_quant=True)
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb,
                                                 device_map={"": 0}, torch_dtype=torch.float16)
    model = prepare_model_for_kbit_training(model)
    lora = LoraConfig(r=a.lora_r, lora_alpha=2 * a.lora_r, lora_dropout=0.05, bias="none",
                      task_type="CAUSAL_LM",
                      target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()

    ds = build_dataset(rows, tok, max_len)
    collator = DataCollatorForLanguageModeling(tok, mlm=False, pad_to_multiple_of=8)
    args = TrainingArguments(output_dir=a.out, num_train_epochs=a.epochs,
                             per_device_train_batch_size=1, gradient_accumulation_steps=8,
                             learning_rate=a.lr, lr_scheduler_type="cosine", warmup_ratio=0.03,
                             logging_steps=10, save_strategy="no", report_to=[],
                             fp16=True, optim="paged_adamw_8bit", gradient_checkpointing=True,
                             dataloader_num_workers=2)
    t0 = time.time()
    Trainer(model=model, args=args, train_dataset=ds, data_collator=collator).train()
    model.save_pretrained(a.out)
    tok.save_pretrained(a.out)
    print("saved adapter to %s in %.1f min" % (a.out, (time.time() - t0) / 60), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
