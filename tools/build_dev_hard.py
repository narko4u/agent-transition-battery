#!/usr/bin/env python3
"""Build a dev family from the tasks the seed instruction fails, and prove it is disjoint.

Saturation is the quiet killer: if the model already solves most of the dev set, an
optimiser has nothing to search and its gains are noise. This takes the scored sweep,
keeps the failures, and refuses to write a family that touches an evaluation family.

  python3 tools/build_dev_hard.py --scores work/seed-scores-devpool.json \
      --family families/mbpp-devhard --n 60 --exclude families/mbpp-hold60 families/mbpp-test60
"""
import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def ids(family_dir):
    d = json.loads((ROOT / family_dir / "family.json").read_text())
    return {t["id"] for t in d["tasks"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scores", required=True)
    ap.add_argument("--family", required=True)
    ap.add_argument("--n", type=int, default=60)
    ap.add_argument("--exclude", nargs="+", default=["families/mbpp-hold60", "families/mbpp-test60"])
    ap.add_argument("--source", default="families/mbpp-devpool")
    a = ap.parse_args()

    scores = json.loads(Path(a.scores).read_text())
    source = json.loads((ROOT / a.source / "family.json").read_text())["tasks"]
    by_id = {t["id"]: t for t in source}

    banned = set()
    for fam in a.exclude:
        banned |= ids(fam)

    failed = [(tid, v) for tid, v in scores["results"].items() if not v["pass"]]
    failed.sort(key=lambda kv: kv[1]["score"])       # hardest first
    chosen = [(tid, v) for tid, v in failed if tid not in banned][: a.n]

    if len(chosen) < 40:
        raise SystemExit("only %d failed tasks available, need at least 40" % len(chosen))

    out = ROOT / a.family
    if out.exists():
        shutil.rmtree(out)
    (out / "tests").mkdir(parents=True)

    tasks = []
    for tid, v in chosen:
        t = dict(by_id[tid])
        src = ROOT / a.source / t["tests"]
        dst = out / t["tests"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)
        t["seed_dense"] = v["score"]
        tasks.append(t)

    idset = {t["id"] for t in tasks}
    leak = idset & banned
    if leak:
        raise SystemExit("REFUSING: %d tasks overlap an evaluation family: %s" % (len(leak), sorted(leak)[:5]))

    fam = {"name": Path(a.family).name,
           "source": "%s, tasks the seed instruction fails, verified disjoint from %s"
                     % (a.source, ", ".join(a.exclude)),
           "n": len(tasks), "seed_pass_rate": 0.0, "tasks": tasks}
    (out / "family.json").write_text(json.dumps(fam, indent=1))
    print("built %s with %d tasks, zero overlap with %s" % (a.family, len(tasks), a.exclude))
    print("seed pass rate on this family is 0 by construction; mean seed dense %.3f"
          % (sum(t["seed_dense"] for t in tasks) / len(tasks)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
