#!/usr/bin/env python3
"""Paired A/B of two solving procedures, same tasks, temperature 0, exact McNemar.

  python3 tools/procedure_ab.py --baseline procedure.md --candidate /tmp/cand.md \
      --families families/python-basics40 families/text-basics --workers 8 \
      --out runs/ab-procedure-2026-11-27.json

Each task is solved once per arm. A task counts as passed when its generated unittest file
passes. The report records per-task outcomes, accuracy, spend and the McNemar exact p so the
promotion gate reads a number rather than an impression.
"""
import argparse
import json
import math
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from adapters.deepseek import DeepSeek  # noqa: E402


def load_tasks(family_dirs):
    out = []
    for fd in family_dirs:
        fam = Path(fd) if Path(fd).is_absolute() else ROOT / fd
        meta = json.loads((fam / "family.json").read_text())
        for t in meta["tasks"]:
            out.append((fam, t))
    return out


def run_one(fam, task, adapter, procedure):
    started = time.time()
    code = ""
    try:
        code = adapter.solve(task, None, procedure)
    except Exception as exc:
        return {"id": task["id"], "pass": False, "detail": "%s: %s" % (type(exc).__name__, exc),
                "seconds": round(time.time() - started, 2)}
    with tempfile.TemporaryDirectory(prefix="ab-") as tmp:
        tmpd = Path(tmp)
        (tmpd / "solution.py").write_text(code or "")
        src = fam / task["tests"]
        (tmpd / "tests").mkdir()
        shutil.copy2(src, tmpd / "tests" / src.name)
        try:
            p = subprocess.run([sys.executable, str(tmpd / "tests" / src.name)], cwd=tmpd,
                               capture_output=True, text=True, timeout=task.get("timeout_s", 30))
            ok = p.returncode == 0
            detail = "" if ok else (p.stderr or p.stdout).strip().splitlines()[-1][:200]
        except subprocess.TimeoutExpired:
            ok, detail = False, "timeout"
    return {"id": task["id"], "pass": ok, "detail": detail,
            "seconds": round(time.time() - started, 2)}


def mcnemar_exact(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** n)
    return round(min(1.0, 2 * tail), 6)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--families", nargs="+", required=True)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    base_proc = Path(a.baseline).read_text()
    cand_proc = Path(a.candidate).read_text()
    tasks = load_tasks(a.families)
    arms = {}
    for name, proc in (("baseline", base_proc), ("candidate", cand_proc)):
        adapter = DeepSeek()
        started = time.time()
        with ThreadPoolExecutor(max_workers=a.workers) as pool:
            rows = list(pool.map(lambda ft: run_one(ft[0], ft[1], adapter, proc), tasks))
        arms[name] = {
            "accuracy": round(sum(1 for r in rows if r["pass"]) / len(rows), 4),
            "passed": sum(1 for r in rows if r["pass"]),
            "of": len(rows),
            "spend_usd": adapter.spend_usd(),
            "wall_s": round(time.time() - started, 1),
            "results": {r["id"]: {"pass": r["pass"], "detail": r["detail"]} for r in rows},
        }
        print("%-9s %d/%d  %.4f  $%.4f  %.0fs" % (name, arms[name]["passed"], len(rows),
                                                  arms[name]["accuracy"], arms[name]["spend_usd"],
                                                  arms[name]["wall_s"]))

    b = sum(1 for t in arms["baseline"]["results"]
            if not arms["baseline"]["results"][t]["pass"] and arms["candidate"]["results"][t]["pass"])
    c = sum(1 for t in arms["baseline"]["results"]
            if arms["baseline"]["results"][t]["pass"] and not arms["candidate"]["results"][t]["pass"])
    p = mcnemar_exact(b, c)
    flipped_to_pass = [t for t in arms["baseline"]["results"]
                       if not arms["baseline"]["results"][t]["pass"] and arms["candidate"]["results"][t]["pass"]]
    flipped_to_fail = [t for t in arms["baseline"]["results"]
                       if arms["baseline"]["results"][t]["pass"] and not arms["candidate"]["results"][t]["pass"]]
    rep = {"schema": "ttb5/ab-report/0.1", "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "model": arms and "deepseek-flash", "tasks": len(tasks),
           "baseline": {"sha256": hashlib_sha(base_proc), "accuracy": arms["baseline"]["accuracy"],
                        "passed": arms["baseline"]["passed"], "spend_usd": arms["baseline"]["spend_usd"]},
           "candidate": {"sha256": hashlib_sha(cand_proc), "accuracy": arms["candidate"]["accuracy"],
                         "passed": arms["candidate"]["passed"], "spend_usd": arms["candidate"]["spend_usd"]},
           "paired": {"b_improved": b, "c_regressed": c, "mcnemar_exact_p": p,
                      "flipped_to_pass": flipped_to_pass, "flipped_to_fail": flipped_to_fail},
           "results": {k: {n: arms[n]["results"][k]["pass"] for n in ("baseline", "candidate")} for k in arms["baseline"]["results"]},
           "total_spend_usd": round(arms["baseline"]["spend_usd"] + arms["candidate"]["spend_usd"], 4)}
    out = ROOT / a.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rep, indent=1) + "\n")
    print("paired: improved %d, regressed %d, exact p %.4f" % (b, c, p))
    print("wrote", out)
    return 0


def hashlib_sha(text: str) -> str:
    import hashlib
    return "sha256:" + hashlib.sha256(text.encode()).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
