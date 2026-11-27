#!/usr/bin/env python3
"""Build the partial-credit variant of the forty-task family.

Same tasks as python-basics40, but each test case becomes its own test method, so a task scores
between 0 and 1 instead of 0 or 1. Fifty tasks at four cases each is two hundred observations,
which is the cheapest way to cut measurement noise without more model calls.
"""
import importlib.util
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location("bf40", ROOT / "build_family40.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
T = mod.T
DEV_IDS = mod.DEV_IDS
HELDOUT_IDS = mod.HELDOUT_IDS

TEMPLATE = '''import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import {entry}


class TestCase(unittest.TestCase):
{cases}


if __name__ == "__main__":
    unittest.main()
'''


def body(cases):
    out = []
    for i, (expr, expected) in enumerate(cases, 1):
        out.append("    def test_case_%d(self):" % i)
        if expected == "ValueError":
            out.append("        with self.assertRaises(ValueError):")
            out.append("            %s" % expr)
        else:
            out.append("        self.assertEqual(%s, %s)" % (expr, expected))
        out.append("")
    return "\n".join(out).rstrip()


def write_family(name, tasks, note):
    d = ROOT / name
    if d.exists():
        shutil.rmtree(d)
    (d / "tests").mkdir(parents=True)
    meta = {"id": name, "verifier": "unittest", "author": "Empire Labs Pty Ltd",
            "note": note, "tasks": []}
    for t in tasks:
        testfile = "tests/test_%s.py" % t["id"]
        (d / testfile).write_text(TEMPLATE.format(entry=t["entry"], cases=body(t["cases"])))
        meta["tasks"].append({"id": t["id"], "entry": t["entry"], "spec": t["spec"],
                              "reference": t["reference"], "tests": testfile,
                              "cases": len(t["cases"]), "timeout_s": 30})
    (d / "family.json").write_text(json.dumps(meta, indent=1) + "\n")
    print("%-30s %d tasks, %d cases" % (name, len(tasks), sum(len(t["cases"]) for t in tasks)))


if __name__ == "__main__":
    by_id = {t["id"]: t for t in T}
    write_family("python-basics40c", T, "All forty tasks, one test method per case.")
    write_family("python-basics40c-dev", [by_id[i] for i in DEV_IDS], "Dev half.")
    write_family("python-basics40c-heldout", [by_id[i] for i in HELDOUT_IDS], "Held-out half.")
