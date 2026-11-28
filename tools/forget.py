#!/usr/bin/env python3
"""Forgetting test. A promotion must not overwrite what was already learned.

arXiv:2610.25858 found that self-modifying agents buy plasticity at the cost of stability: global
edits to a shared prompt or workspace interfere with earlier tasks. We had no test for that, so an
accepted procedure could quietly cost performance on an older family and nothing would notice.

This gate runs the incumbent and the accepted candidate on an OLD family, with the same tasks and the
same tests, and refuses if the candidate is worse by more than the noise band. A promotion passes only
when the new procedure is no worse on the old work than the procedure it replaced.

  python3 tools/forget.py --family families/python-basics40-dev --adapter bon3 --out runs/forget-1.json
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOLERANCE_FLOOR = 0.05


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--adapter", default="bon3")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    tmp = Path(a.out).with_suffix(".ab.json")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    proc = ROOT / "PROCEDURE.md"
    if not proc.exists():
        print("no PROCEDURE.md; the forgetting test compares procedure text plus adapter")
        return 2
    cmd = [sys.executable, str(ROOT / "tools" / "procedure_ab.py"),
           "--baseline", str(proc), "--candidate", str(proc),
           "--baseline-adapter", "deepseek", "--adapter", a.adapter,
           "--families", a.family,
           "--workers", str(a.workers), "--out", str(tmp)]
    print("running: " + " ".join(cmd[-8:]), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-1500:] + r.stderr[-1500:])
        print("forgetting test could not run; refusing to pass it")
        return 2

    ab = json.loads(tmp.read_text())
    base = ab["baseline"]["accuracy"]
    cand = ab["candidate"]["accuracy"]
    sd = ab.get("sd") or 0.0
    tol = max(2 * sd, TOLERANCE_FLOOR)
    delta = round(cand - base, 4)
    forgot = cand < base - tol
    report = {"kind": "forgetting", "family": a.family, "adapter": a.adapter,
              "incumbent": base, "accepted": cand, "delta": delta,
              "tolerance": round(tol, 4), "verdict": "forgot" if forgot else "no-forgetting",
              "note": "one-sided: only a regression counts against the candidate"}
    Path(a.out).write_text(json.dumps(report, indent=1) + "\n")
    print(json.dumps(report, indent=1))
    print("REFUSED: the accepted procedure is worse on earlier work by %.1f points"
          % ((base - cand) * 100) if forgot else
          "PASS: no forgetting detected on %s" % a.family)
    return 1 if forgot else 0


if __name__ == "__main__":
    raise SystemExit(main())
