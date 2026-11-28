#!/usr/bin/env python3
"""Score two instructions on a frozen family: one-shot, executed tests, exact McNemar.

  python3 tools/instruction_eval.py --family families/mbpp-hold60 \
      --base-instruction seed.txt --tuned-instruction evolved.txt \
      --protocol P-004 --out runs/gepa-hold60.json

Base and tuned differ only in the instruction text. Same model, same tasks,
same tests, same order for every task. No weights are touched.
"""
import argparse
import json
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lm import Meter, extract_code  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def run_one(meter, instruction, task, fam_dir):
    user = ("Task: %s\n\nDefine exactly the function named %s. "
            "Return only Python code in one fenced block."
            % (task["spec"], task.get("entry", task["id"])))
    try:
        code = extract_code(meter.chat(instruction, user, max_tokens=900))
    except SystemExit:
        raise
    except Exception as e:
        return False, "solver error %r" % (e,)
    with tempfile.TemporaryDirectory(prefix="ie-") as td:
        p = Path(td)
        (p / "solution.py").write_text(code)
        t = p / Path(task["tests"]).name
        t.write_text((fam_dir / task["tests"]).read_text())
        try:
            r = subprocess.run([sys.executable, str(t)], cwd=td,
                               capture_output=True, text=True, timeout=30)
            return r.returncode == 0, "" if r.returncode == 0 else (r.stderr or "")[-300:]
        except subprocess.TimeoutExpired:
            return False, "timeout"


def arm(meter, instruction, tasks, fam_dir, workers):
    with ThreadPoolExecutor(max_workers=workers) as ex:
        res = list(ex.map(lambda t: run_one(meter, instruction, t, fam_dir), tasks))
    return {t["id"]: {"pass": ok, "err": err} for t, (ok, err) in zip(tasks, res)}


def mcnemar(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = max(b, c)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", required=True)
    ap.add_argument("--base-instruction", required=True)
    ap.add_argument("--tuned-instruction", required=True)
    ap.add_argument("--protocol", default="P-004")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--cap-usd", type=float, default=0.60)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    fam_dir = ROOT / a.family
    fam = json.loads((fam_dir / "family.json").read_text())
    tasks = fam["tasks"]
    base_instr = Path(a.base_instruction).read_text()
    tuned_instr = Path(a.tuned_instruction).read_text()

    meter = Meter(a.cap_usd)
    t0 = time.time()
    base = arm(meter, base_instr, tasks, fam_dir, a.workers)
    tuned = arm(meter, tuned_instr, tasks, fam_dir, a.workers)

    bp = sum(1 for v in base.values() if v["pass"])
    tp = sum(1 for v in tuned.values() if v["pass"])
    up = sum(1 for k in base if tuned[k]["pass"] and not base[k]["pass"])
    dn = sum(1 for k in base if base[k]["pass"] and not tuned[k]["pass"])
    p = mcnemar(up, dn)
    delta = round((tp - bp) / len(tasks), 4)

    out = {
        "kind": "procedure",
        "date": time.strftime("%Y-%m-%d"),
        "model": "deepseek-flash",
        "family": a.family,
        "order": "base-first",
        "base": {"passed": bp, "of": len(tasks), "accuracy": round(bp / len(tasks), 4)},
        "tuned": {"passed": tp, "of": len(tasks), "accuracy": round(tp / len(tasks), 4)},
        "delta": delta,
        "improved": up,
        "regressed": dn,
        "mcnemar_exact_p": round(p, 4),
        "protocol_id": a.protocol,
        "spend_usd": round(meter.usd, 4),
        "minutes": round((time.time() - t0) / 60, 1),
        "results": {"base": base, "tuned": tuned},
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print("%s base %d/%d tuned %d/%d delta %+.4f up %d dn %d p %.4f spend $%.3f"
          % (a.family, bp, len(tasks), tp, len(tasks), delta, up, dn, p, meter.usd), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
