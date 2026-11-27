#!/usr/bin/env python3
"""Build an MBPP-backed family. Public benchmark, human-curated tests, real statistical power.

Source: MBPP sanitized, 427 problems, CC-BY-4.0, Austin et al. 2021.
https://github.com/google-research/google-research/tree/master/mbpp

    python3 families/build_mbpp_family.py /tmp/mbpp.json [--limit N] [--name mbpp-basics]

Each problem becomes a family task: the prompt is the spec, the dataset solution is the reference
and the dataset assertions become a unittest file. No reference is edited to make a test pass.
"""
import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TEMPLATE = '''import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import {entry}  # noqa: F401
{imports}


class TestCase(unittest.TestCase):
    def test_cases(self):
{cases}


if __name__ == "__main__":
    unittest.main()
'''


def entry_of(code: str) -> str:
    m = re.search(r"^\s*def\s+(\w+)\s*\(", code, re.M)
    return m.group(1) if m else ""


def build(rows, name, limit):
    d = ROOT / name
    if d.exists():
        shutil.rmtree(d)
    (d / "tests").mkdir(parents=True)
    meta = {"id": name, "verifier": "unittest", "author": "Empire Labs Pty Ltd",
            "source": "MBPP sanitized, CC-BY-4.0, Austin et al. 2021",
            "note": "Public benchmark. Tests come from the dataset, not from our reference.",
            "tasks": []}
    kept = 0
    for r in rows:
        if limit and kept >= limit:
            break
        entry = entry_of(r["code"])
        if not entry or not r.get("test_list"):
            continue
        tid = "mbpp_%s" % r["task_id"]
        testfile = "tests/test_%s.py" % tid
        imports = "\n".join(r.get("test_imports") or [])
        body = "\n".join("        %s" % line.strip() for line in r["test_list"])
        (d / testfile).write_text(TEMPLATE.format(entry=entry, imports=imports, cases=body))
        meta["tasks"].append({"id": tid, "entry": entry,
                              "spec": r["prompt"].strip() + "\n\nDefine the function as `%s`." % entry,
                              "reference": re.split(r"\n={4,}\n", r["code"])[0].rstrip() + "\n", "tests": testfile,
                              "cases": len(r["test_list"]), "timeout_s": 30})
        kept += 1
    (d / "family.json").write_text(json.dumps(meta, indent=1) + "\n")
    print("%-20s %d tasks" % (name, kept))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--name", default="mbpp-basics")
    a = ap.parse_args()
    build(json.loads(Path(a.source).read_text()), a.name, a.limit)
