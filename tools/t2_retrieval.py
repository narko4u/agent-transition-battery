#!/usr/bin/env python3
"""T2 by retrieval: does showing similar solved problems beat writing prose lessons?

Practice block solves sixty MBPP tasks and keeps the passing solutions. The test block is sixty
different tasks in the same domain. Three arms:

  control     plain solve
  similar     the two most lexically similar solved practice problems, spec and code, in context
  random      two solved practice problems chosen at random, same length

The random arm is the control that matters: both exemplar arms spend the same tokens, so any gain
in `similar` over `random` is the value of similarity, not of extra context.

    python3 tools/t2_retrieval.py --practice families/mbpp-practice60 --test families/mbpp-test60
"""
import argparse
import difflib
import json
import random
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import ttb  # noqa: E402
from adapters.deepseek import DeepSeek, extract_code, IN_PER_M, OUT_PER_M  # noqa: E402


def tokens(s):
    return set(re.findall(r"[a-z_]+", s.lower()))


def similarity(a, b):
    ta, tb = tokens(a), tokens(b)
    jac = len(ta & tb) / max(1, len(ta | tb))
    return 0.5 * jac + 0.5 * difflib.SequenceMatcher(None, a[:600], b[:600]).ratio()


class Exemplar(DeepSeek):
    """DeepSeek with a fixed set of worked examples prepended to every prompt."""

    k: int = 2
    pick: str = "similar"

    def __init__(self):
        super().__init__()
        self.examples = []

    def solve(self, task, store=None, procedure=""):
        if not self.examples:
            return super().solve(task, store, procedure)
        blocks = []
        for e in self.examples:
            blocks.append("Example task: %s\n\n%s\n\nA solution:\n```python\n%s```"
                          % (e["id"], e["spec"][:500], e["code"]))
        user = ("%s\n\nNow solve this task. Return only Python code in one fenced block. Define exactly "
                "the function named %s.\n\nTask: %s\n\n%s"
                % ("\n\n".join(blocks), task.get("entry", task["id"]), task["id"], task["spec"]))
        return extract_code(self._chat("You write Python. Worked examples are shown.", user,
                                       max_tokens=1200))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--practice", default="families/mbpp-practice60")
    ap.add_argument("--test", default="families/mbpp-test60")
    ap.add_argument("--k", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    started = time.time()
    practice = ttb.load_family(ROOT / a.practice)
    test = ttb.load_family(ROOT / a.test)

    # 1. practice block: solve, keep what passed
    proc = (ROOT / "procedure.md").read_text()
    prac_adapter = DeepSeek()
    prac = ttb.evaluate(practice, prac_adapter, proc, workers=4, keep_code=True)
    solved = []
    for t in practice["tasks"]:
        r = prac["results"][t["id"]]
        if r["pass"] and r.get("code"):
            solved.append({"id": t["id"], "spec": t["spec"], "code": r["code"]})
    print("practice: %d/%d passed, %d usable examples" % (prac["passed"], prac["of"], len(solved)))

    # 2. three arms on the unseen test block
    arms = {}
    for name in ("control", "similar", "random"):
        ad = Exemplar()
        if name in ("similar", "random"):
            ad.k = a.k
            ad.pick = name
        arms[name] = ad

    results = {}
    for name, ad in arms.items():
        if name != "control":
            assign_examples(ad, solved, test, a.seed)
            ad.spend_before = (ad.pt, ad.ct)
        res = ttb.evaluate(test, ad, proc, workers=4)
        results[name] = res
        print("%-8s %d/%d %.4f" % (name, res["passed"], res["of"], res["accuracy"]))

    # 3. paired comparisons
    def pair(x, y):
        up = down = 0
        for t in test["tasks"]:
            a_, b_ = results[x]["results"][t["id"]]["pass"], results[y]["results"][t["id"]]["pass"]
            up += (a_ and not b_)
            down += (b_ and not a_)
        return up, down

    up_c, dn_c = pair("similar", "control")
    up_r, dn_r = pair("similar", "random")
    report = {
        "kind": "t2-retrieval",
        "date": time.strftime("%Y-%m-%d"),
        "practice": a.practice, "test": a.test, "k": a.k, "seed": a.seed,
        "practice_result": {"passed": prac["passed"], "of": prac["of"]},
        "examples": len(solved),
        "arms": {n: {"passed": r["passed"], "of": r["of"], "accuracy": r["accuracy"]}
                 for n, r in results.items()},
        "similar_vs_control": {"improved": up_c, "regressed": dn_c,
                               "delta": round(results["similar"]["accuracy"] - results["control"]["accuracy"], 4)},
        "similar_vs_random": {"improved": up_r, "regressed": dn_r,
                              "delta": round(results["similar"]["accuracy"] - results["random"]["accuracy"], 4)},
        "spend_usd": round(sum((x.pt * IN_PER_M + x.ct * OUT_PER_M) / 1e6
                               for x in list(arms.values()) + [prac_adapter]), 4),
        "seconds": round(time.time() - started, 1),
    }
    report["status"] = ("pass" if report["similar_vs_control"]["delta"] >= 0.05 else "fail")
    Path(a.out).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("similar_vs_control", "similar_vs_random", "spend_usd", "status")}, indent=1))
    return 0


def assign_examples(ad, solved, test, seed):
    if ad.pick == "random":
        rng = random.Random(seed)
        pool = list(solved)
        rng.shuffle(pool)
        ad.examples = pool[:ad.k]
        return
    out = []
    for t in test["tasks"]:
        ranked = sorted(solved, key=lambda s: -similarity(t["spec"], s["spec"]))
        out.append((t["id"], ranked[:ad.k]))
    ad.per_task = {tid: ex for tid, ex in out}
    ad.examples = out[0][1]
    ad.solve = _per_task_solve.__get__(ad, type(ad))


def _per_task_solve(self, task, store=None, procedure=""):
    ex = getattr(self, "per_task", {}).get(task["id"]) or self.examples
    blocks = ["Example task: %s\n\n%s\n\nA solution:\n```python\n%s```" % (e["id"], e["spec"][:500], e["code"])
              for e in ex]
    user = ("%s\n\nNow solve this task. Return only Python code in one fenced block. Define exactly "
            "the function named %s.\n\nTask: %s\n\n%s"
            % ("\n\n".join(blocks), task.get("entry", task["id"]), task["id"], task["spec"]))
    return extract_code(self._chat("You write Python. Worked examples are shown.", user, max_tokens=1200))


if __name__ == "__main__":
    raise SystemExit(main())
