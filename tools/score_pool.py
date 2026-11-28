#!/usr/bin/env python3
"""Score the seed instruction over a family, task by task, and keep the verdicts.

Used to pick a deviation-free dev set: tasks the model already solves carry no
signal for an optimiser, so they are filtered out before any search begins.

  python3 tools/score_pool.py --family families/mbpp-devpool --out work/seed-scores.json
"""
import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gepa_v2 import SEED, prompt_for, score_dense  # noqa: E402
from lm import Meter, extract_code  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def one(args):
    meter, system, task, fam_dir = args
    user = ("Task: %s\n\nDefine exactly the function named %s. "
            "Return only Python code in one fenced block."
            % (task["spec"], task.get("entry", task["id"])))
    code = extract_code(meter.chat(system, user, max_tokens=3000))
    sc, fb = score_dense(code, fam_dir / task["tests"])
    return task["id"], {"score": sc, "pass": sc >= 0.99, "chars": len(code), "feedback": fb[:300]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--cap-usd", type=float, default=0.80)
    a = ap.parse_args()

    fam_dir = ROOT / a.family
    tasks = json.loads((fam_dir / "family.json").read_text())["tasks"]
    meter = Meter(a.cap_usd)
    system = prompt_for(SEED)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        rows = dict(ex.map(one, [(meter, system, t, fam_dir) for t in tasks]))

    passed = sum(1 for v in rows.values() if v["pass"])
    empty = sum(1 for v in rows.values() if v["chars"] < 5)
    out = {"family": a.family, "n": len(tasks), "passed": passed,
           "accuracy": round(passed / len(tasks), 4), "empty_completions": empty,
           "empties_meter": meter.empties, "spend_usd": round(meter.usd, 4),
           "minutes": round((time.time() - t0) / 60, 1), "results": rows}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print("passed %d/%d = %.4f, empty %d, spend $%.3f, %.1f min"
          % (passed, len(tasks), passed / len(tasks), empty, meter.usd, out["minutes"]), flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
