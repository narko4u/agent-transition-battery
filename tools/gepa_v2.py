#!/usr/bin/env python3
"""GEPA v2: the five fixes from P-004's failure, in one experiment.

What changed against v1, and why:
  1. Dense score. Partial credit for the assert that failed, not binary pass.
     A binary metric on 60 tasks rewards flipping the cheapest failure.
  2. Internal split. 40 train / 20 validation inside the dev family, so a
     candidate is accepted on data it was not proposed against.
  3. Two text components, instruction and checklist, so the search can move
     procedure as well as wording.
  4. Ceiling tasks dropped from the training split only. Tasks the seed already
     passes carry no signal and inflate variance.
  5. Nothing from the evaluation families is visible here at any point.

  python3 tools/gepa_v2.py --max-calls 700 --out runs/gepa-v2.json
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import gepa
from gepa import EvaluationBatch, GEPAAdapter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lm import Meter, extract_code  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FAMILY = "families/mbpp-practice60"

SEED = {
    "instruction": (
        "You write one Python function per task. Read the whole task before writing.\n"
        "Rules learned the hard way:\n"
        "- Read every constraint, especially about types, duplicates, order and empty input.\n"
        "- Prefer the standard library over hand-rolled loops.\n"
        "- Keep duplicates when the task does not say to remove them.\n"
        "- Return only Python code in one fenced block, defining exactly the named function."
    ),
    "checklist": (
        "Before returning, check: right function name, no prints instead of returns, "
        "no module-level side effects, every stated constraint honoured."
    ),
}


def prompt_for(candidate):
    return candidate["instruction"].strip() + "\n\nChecklist:\n" + candidate["checklist"].strip()


def score_dense(code, test_path):
    """Partial credit: how far into the assertions the candidate got."""
    text = Path(test_path).read_text()
    total = max(1, len(re.findall(r"^\s*assert\b", text, re.M)))
    with tempfile.TemporaryDirectory(prefix="gp2-") as td:
        p = Path(td)
        (p / "solution.py").write_text(code)
        t = p / "tests.py"
        t.write_text(text)
        try:
            r = subprocess.run([sys.executable, str(t)], cwd=td,
                               capture_output=True, text=True, timeout=30)
        except subprocess.TimeoutExpired:
            return 0.0, "timed out after 30s"
        if r.returncode == 0:
            return 1.0, "all %d assertions passed" % total
        err = (r.stderr or r.stdout or "")
        # The traceback names the failing line inside tests.py; count asserts before it.
        hit = re.search(r'tests\.py", line (\d+)', err)
        reached = 0
        if hit:
            upto = "\n".join(text.splitlines()[: int(hit.group(1))])
            reached = len(re.findall(r"^\s*assert\b", upto, re.M))
        score = max(0.0, (reached - 1) / total) if hit else 0.0
        tail = "\n".join(err.strip().splitlines()[-5:])[-600:]
        return round(min(score, 0.99), 4), "failed at assertion %d of %d: %s" % (
            max(reached, 1), total, tail)


class Adapter(GEPAAdapter):
    def __init__(self, fam_dir, meter, max_new=3000):
        self.fam_dir = fam_dir
        self.meter = meter
        self.max_new = max_new
        self.empties = 0

    def evaluate(self, batch, candidate, capture_traces=False):
        system = prompt_for(candidate)
        scores, outputs, trajs = [], [], []
        for t in batch:
            user = ("Task: %s\n\nDefine exactly the function named %s. "
                    "Return only Python code in one fenced block."
                    % (t["spec"], t.get("entry", t["id"])))
            try:
                code = ""
                for attempt in range(3):
                    code = extract_code(self.meter.chat(system, user, max_tokens=self.max_new))
                    if code.strip():
                        break
                    self.empties += 1
                sc, fb = score_dense(code, self.fam_dir / t["tests"])
            except SystemExit:
                raise
            except Exception as e:
                code, sc, fb = "", 0.0, "solver error %r" % (e,)
            scores.append(sc)
            outputs.append({"code": code, "score": sc})
            if capture_traces:
                trajs.append({"task_id": t["id"], "spec": t["spec"], "code": code,
                              "feedback": fb, "score": sc})
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
                "Feedback": ("score %.2f. " % sc) + tr.get("feedback", "")[:700],
            })
        return {c: rows for c in components_to_update}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", default=FAMILY)
    ap.add_argument("--max-calls", type=int, default=700)
    ap.add_argument("--minibatch", type=int, default=3)
    ap.add_argument("--cap-usd", type=float, default=1.20)
    ap.add_argument("--out", required=True)
    ap.add_argument("--run-dir", default="/home/vault/work/gepa-v2")
    ap.add_argument("--protocol", default="P-005")
    ap.add_argument("--no-drop-ceiling", action="store_true")
    a = ap.parse_args()

    fam_dir = ROOT / a.family
    tasks = json.loads((fam_dir / "family.json").read_text())["tasks"]
    train, val = tasks[:40], tasks[40:]
    meter = Meter(a.cap_usd)
    adapter = Adapter(fam_dir, meter)

    if not a.no_drop_ceiling:
        system = prompt_for(SEED)
        keep = []
        for t in train:
            code = extract_code(meter.chat(system,
                                           "Task: %s\n\nDefine exactly the function named %s. "
                                           "Return only Python code in one fenced block."
                                           % (t["spec"], t.get("entry", t["id"])),
                                           max_tokens=3000))
            sc, _ = score_dense(code, fam_dir / t["tests"])
            if sc < 0.99:
                keep.append(t)
        print("ceiling filter: kept %d of %d training tasks" % (len(keep), len(train)), flush=True)
        train = keep or train

    t0 = time.time()
    result = gepa.optimize(
        seed_candidate=SEED,
        trainset=train,
        valset=val,
        adapter=adapter,
        reflection_lm=lambda p: meter.chat(
            "You improve the instructions and checklist for a code-writing agent. "
            "Return only the improved text for the component being revised.",
            p if isinstance(p, str) else json.dumps(p),
            max_tokens=1200, temperature=0.3),
        max_metric_calls=a.max_calls,
        reflection_minibatch_size=a.minibatch,
        candidate_selection_strategy="pareto",
        frontier_type="instance",
        display_progress_bar=False,
        run_dir=a.run_dir,
        seed=0,
    )

    best = result.best_candidate
    combined = prompt_for(best)
    Path("/home/vault/work/instr-gepa-v2.txt").write_text(combined)
    out = {
        "protocol_id": a.protocol,
        "family": a.family,
        "train_tasks": len(train),
        "val_tasks": len(val),
        "metric_calls": a.max_calls,
        "total_metric_calls": getattr(result, "total_metric_calls", None),
        "num_candidates": getattr(result, "num_candidates", None),
        "best_candidate": best,
        "combined_instruction": combined,
        "spend_usd": round(meter.usd, 4),
        "lm_calls": meter.calls,
        "empty_completions": adapter.empties,
        "minutes": round((time.time() - t0) / 60, 1),
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print("candidates %s  spend $%.3f  %.1f min" % (out["num_candidates"], meter.usd, out["minutes"]), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
