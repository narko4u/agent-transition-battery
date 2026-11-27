#!/usr/bin/env python3
"""Decide whether a procedure change has earned promotion.

Runs the same A/B ROUNDS times, then applies the rule measured in MEASUREMENT.md:

    candidate mean >= baseline mean + 2 * sd(baseline rounds)

with a positive difference required as well. One round is an anecdote. Three rounds of majority
of three is the cheapest design that can tell a seven point gain from temperature-zero noise.

    python3 tools/decide.py --baseline procedure.md --candidate cand.md \
        --families families/python-basics40 --rounds 3 --samples 3 \
        --out runs/decision-2026-11-27.json

Offline, from existing reports:

    python3 tools/decide.py --from-reports runs/a.json runs/b.json runs/c.json
"""
import argparse
import json
import statistics as st
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_SD = 0.02      # measured noise floor, so three rounds cannot invent a tiny sigma
MIN_DELTA = 0.05   # below five points this suite cannot see, whatever the arithmetic says


def run_round(baseline, candidate, families, samples, workers, out, adapter="deepseek"):
    cmd = [sys.executable, str(ROOT / "tools" / "procedure_ab.py"),
           "--baseline", baseline, "--candidate", candidate,
           "--families", *families, "--samples", str(samples), "--adapter", adapter,
           "--workers", str(workers), "--out", str(out)]
    if samples > 1:
        pass
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("round failed: %s" % (r.stderr or r.stdout)[-400:])
    return json.loads((ROOT / out).read_text())


def verdict(reports):
    base = [r["baseline"]["accuracy"] for r in reports]
    cand = [r["candidate"]["accuracy"] for r in reports]
    sd = max(st.stdev(base), MIN_SD) if len(base) > 1 else MIN_SD
    threshold = max(st.mean(base) + 2 * sd, st.mean(base) + MIN_DELTA)
    passed = st.mean(cand) > st.mean(base) and st.mean(cand) >= threshold
    return {
        "baseline_rounds": base, "candidate_rounds": cand,
        "baseline_mean": round(st.mean(base), 4), "baseline_sd": round(sd, 4),
        "candidate_mean": round(st.mean(cand), 4),
        "threshold": round(threshold, 4), "delta": round(st.mean(cand) - st.mean(base), 4),
        "verdict": "PASS" if passed else "FAIL",
        "spend_usd": round(sum(r.get("total_spend_usd", 0) for r in reports), 4),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline")
    ap.add_argument("--candidate")
    ap.add_argument("--families", nargs="+")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--adapter", default="deepseek", choices=["deepseek", "selfcheck", "bon3", "bon5", "bon3r"])
    ap.add_argument("--out", default="")
    ap.add_argument("--from-reports", nargs="+")
    a = ap.parse_args()

    if a.from_reports:
        reports = [json.loads(Path(p).read_text()) for p in a.from_reports]
    else:
        if not (a.baseline and a.candidate and a.families):
            raise SystemExit("need --baseline --candidate --families, or --from-reports")
        reports = []
        for i in range(a.rounds):
            out = "runs/decide-round-%d.json" % (i + 1)
            print("round %d/%d" % (i + 1, a.rounds))
            reports.append(run_round(a.baseline, a.candidate, a.families, a.samples,
                                     a.workers, out, a.adapter))
    v = verdict(reports)
    print(json.dumps(v, indent=1))
    if a.out:
        p = ROOT / a.out
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                 "rounds": len(reports), **v}, indent=1) + "\n")
        print("wrote", p)
    return 0 if v["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
