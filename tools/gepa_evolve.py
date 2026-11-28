#!/usr/bin/env python3
"""Evolve the solver instruction with GEPA, scored by executing real tests.

GEPA (MIT, gepa-ai/gepa) reflects on failures and proposes a better instruction.
We give it the only metric that counts here: hidden tests executed in a sandbox.

  python3 tools/gepa_evolve.py --family families/mbpp-practice60 \
      --max-calls 300 --out runs/gepa-practice60.json

Nothing in the evaluation families is touched. The evolved instruction is a
candidate like any other and still has to pass the gate on hold60 and test60.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

import gepa
from gepa import EvaluationBatch, GEPAAdapter

from lm import Meter, extract_code

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("TTB_MODEL", "deepseek-flash")
BASE = os.environ.get("TTB_BASE_URL", "https://api.deepseek.com/v1")
IN_PER_M, OUT_PER_M = 0.28, 0.42

SEED = """You are a Python function writer. Read the task, then write the function.

Rules learned the hard way:
- Read every constraint in the task, especially about types, duplicates, order and empty inputs.
- Prefer the standard library over hand-rolled loops.
- Keep duplicates when the task does not say to remove them.
- Return only Python code in one fenced block, and define exactly the named function."""


def score(code, test_path):
    """Run the family's own test file against the candidate code."""
    with tempfile.TemporaryDirectory(prefix="gp-") as td:
        p = Path(td)
        (p / "solution.py").write_text(code)
        t = p / Path(test_path).name
        t.write_text(Path(test_path).read_text())
        try:
            r = subprocess.run([sys.executable, str(t)], cwd=td,
                               capture_output=True, text=True, timeout=30)
        except subprocess.TimeoutExpired:
            return False, "timed out after 30s"
        if r.returncode == 0:
            return True, "all tests passed"
        err = (r.stderr or r.stdout or "").strip().splitlines()
        tail = "\n".join(err[-6:]) if err else "non-zero exit, no output"
        return False, tail[-800:]


class CodeAdapter(GEPAAdapter):
    def __init__(self, tasks, fam_dir, meter, max_new=900):
        self.tasks = tasks
        self.fam_dir = fam_dir
        self.meter = meter
        self.max_new = max_new

    def solve(self, instruction, task):
        user = ("Task: %s\n\nDefine exactly the function named %s. "
                "Return only Python code in one fenced block."
                % (task["spec"], task.get("entry", task["id"])))
        return extract_code(self.meter.chat(instruction, user, max_tokens=self.max_new))

    def evaluate(self, batch, candidate, capture_traces=False):
        instruction = candidate["instruction"]
        scores, outputs, trajs = [], [], []
        for t in batch:
            try:
                code = self.solve(instruction, t)
                ok, feedback = score(code, self.fam_dir / t["tests"])
            except SystemExit:
                raise
            except Exception as e:
                code, ok, feedback = "", False, "solver error: %r" % (e,)
            scores.append(1.0 if ok else 0.0)
            outputs.append({"code": code, "pass": ok})
            if capture_traces:
                trajs.append({"task_id": t["id"], "spec": t["spec"],
                              "code": code, "feedback": feedback, "pass": ok})
        return EvaluationBatch(outputs=outputs, scores=scores,
                               trajectories=trajs if capture_traces else None,
                               num_metric_calls=len(batch))

    def make_reflective_dataset(self, candidate, eval_batch, components_to_update):
        rows = []
        for out, sc, tr in zip(eval_batch.outputs, eval_batch.scores,
                               eval_batch.trajectories or []):
            rows.append({
                "Inputs": {"task": tr.get("spec", "")[:1200]},
                "Generated Outputs": {"code": out["code"][:1600]},
                "Feedback": ("PASS" if sc == 1.0 else "FAIL: " + tr.get("feedback", "")[:800]),
            })
        return {c: rows for c in components_to_update}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", default="families/mbpp-practice60")
    ap.add_argument("--max-calls", type=int, default=300)
    ap.add_argument("--minibatch", type=int, default=3)
    ap.add_argument("--cap-usd", type=float, default=1.50)
    ap.add_argument("--out", required=True)
    ap.add_argument("--run-dir", default="")
    ap.add_argument("--seed-instruction", default="")
    ap.add_argument("--protocol", default="P-004")
    a = ap.parse_args()

    fam_dir = ROOT / a.family
    fam = json.loads((fam_dir / "family.json").read_text())
    tasks = fam["tasks"]
    meter = Meter(a.cap_usd)
    adapter = CodeAdapter(tasks, fam_dir, meter)
    seed = Path(a.seed_instruction).read_text() if a.seed_instruction else SEED

    t0 = time.time()
    result = gepa.optimize(
        seed_candidate={"instruction": seed},
        trainset=tasks,
        valset=tasks,
        adapter=adapter,
        reflection_lm=lambda prompt: meter.chat(
            "You improve instructions for a code-writing agent. "
            "Return only the new instruction text.",
            prompt if isinstance(prompt, str) else json.dumps(prompt),
            max_tokens=1200, temperature=0.3),
        max_metric_calls=a.max_calls,
        reflection_minibatch_size=a.minibatch,
        candidate_selection_strategy="pareto",
        display_progress_bar=False,
        run_dir=a.run_dir or None,
        seed=0,
    )

    best = result.best_candidate["instruction"]
    scores = getattr(result, "val_aggregate_subscores", None) or []
    best_score = None
    try:
        idx = result.best_idx
        if scores and idx is not None:
            v = scores[idx]
            if isinstance(v, dict):
                vals = [x for x in v.values() if isinstance(x, (int, float))]
                best_score = round(sum(vals) / len(vals), 4) if vals else None
            elif isinstance(v, (int, float)):
                best_score = round(float(v), 4)
    except Exception:
        best_score = None
    out = {
        "protocol_id": a.protocol,
        "family": a.family,
        "tasks": len(tasks),
        "metric_calls": a.max_calls,
        "total_metric_calls": getattr(result, "total_metric_calls", None),
        "num_candidates": getattr(result, "num_candidates", None),
        "best_idx": getattr(result, "best_idx", None),
        "best_score": best_score,
        "best_instruction": best,
        "seed_instruction": seed,
        "spend_usd": round(meter.usd, 4),
        "lm_calls": meter.calls,
        "prompt_tokens": meter.prompt_tokens,
        "completion_tokens": meter.completion_tokens,
        "minutes": round((time.time() - t0) / 60, 1),
        "model": MODEL,
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print("best_score %s  spend $%.4f  %d calls  %.1f min"
          % (out["best_score"], meter.usd, meter.calls, out["minutes"]), flush=True)
    print("wrote", a.out, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
