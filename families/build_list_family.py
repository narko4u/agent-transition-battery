#!/usr/bin/env python3
"""Build the list-basics family, the third surface for T3.

Same procedure as the other families on sequences: read a spec, handle the stated edge cases,
return a pure function.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
T = []


def task(tid, entry, spec, ref, cases):
    T.append({"id": tid, "entry": entry, "spec": spec.strip(), "reference": ref.strip(),
              "cases": cases})


task("interleave", "interleave", """
Write interleave(a, b) -> list. Take elements alternately from a then b, and append whatever is
left of the longer sequence at the end.
""", """
def interleave(a, b):
    a, b = list(a), list(b)
    out = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            out.append(a[i])
        if i < len(b):
            out.append(b[i])
    return out
""", [
    ('interleave([1, 2, 3], ["a", "b"])', "[1, 'a', 2, 'b', 3]"),
    ('interleave([], [1, 2])', '[1, 2]'),
    ('interleave([], [])', '[]'),
])

task("dedupe_adjacent", "dedupe_adjacent", """
Write dedupe_adjacent(seq) -> list. Remove consecutive duplicates, keeping the first of each run.
Non-consecutive repeats stay.
""", """
def dedupe_adjacent(seq):
    out = []
    for x in seq:
        if not out or out[-1] != x:
            out.append(x)
    return out
""", [
    ('dedupe_adjacent([1, 1, 2, 3, 3, 3, 2])', '[1, 2, 3, 2]'),
    ('dedupe_adjacent([])', '[]'),
    ('dedupe_adjacent(["a"])', "['a']"),
])

task("longest_run", "longest_run", """
Write longest_run(seq) -> int. Return the length of the longest run of identical consecutive
values. An empty sequence is 0.
""", """
def longest_run(seq):
    best = run = 0
    prev = None
    for x in seq:
        if run and x == prev:
            run += 1
        else:
            run = 1
        prev = x
        best = max(best, run)
    return best
""", [
    ('longest_run([1, 1, 2, 3, 3, 3])', '3'),
    ('longest_run([])', '0'),
    ('longest_run([4])', '1'),
    ('longest_run([1, 2, 1, 2])', '1'),
])

task("sliding_max", "sliding_max", """
Write sliding_max(nums, k) -> list. For each window of k consecutive values return the largest.
Raise ValueError when k is not positive or larger than the list.
""", """
def sliding_max(nums, k):
    nums = list(nums)
    if not isinstance(k, int) or k <= 0 or k > len(nums):
        raise ValueError(k)
    return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]
""", [
    ('sliding_max([1, 3, 2, 5, 4], 2)', '[3, 3, 5, 5]'),
    ('sliding_max([5], 1)', '[5]'),
    ('sliding_max([1, 2], 3)', 'ValueError'),
    ('sliding_max([1, 2], 0)', 'ValueError'),
])

task("partition", "partition", """
Write partition(nums, threshold) -> tuple of two lists. First the values below threshold, then the
values at or above it, each in their original order.
""", """
def partition(nums, threshold):
    low, high = [], []
    for x in nums:
        (low if x < threshold else high).append(x)
    return low, high
""", [
    ('partition([1, 5, 2, 8], 4)', '([1, 2], [5, 8])'),
    ('partition([], 1)', '([], [])'),
    ('partition([3], 3)', '([], [3])'),
])

task("flatten_depth", "flatten_depth", """
Write flatten_depth(seq, depth) -> list. Flatten nested lists and tuples up to depth levels.
depth 0 returns the input as a list. Negative depth raises ValueError.
""", """
def flatten_depth(seq, depth):
    if not isinstance(depth, int) or depth < 0:
        raise ValueError(depth)
    out = []
    for x in seq:
        if depth > 0 and isinstance(x, (list, tuple)):
            out.extend(flatten_depth(x, depth - 1))
        else:
            out.append(x)
    return out
""", [
    ('flatten_depth([1, [2, [3, [4]]]], 1)', '[1, 2, [3, [4]]]'),
    ('flatten_depth([1, [2, [3, [4]]]], 9)', '[1, 2, 3, 4]'),
    ('flatten_depth([1, [2]], 0)', '[1, [2]]'),
    ('flatten_depth([1], -1)', 'ValueError'),
])

task("remove_dupes_keep_last", "remove_dupes_keep_last", """
Write remove_dupes_keep_last(seq) -> list. Keep only the last occurrence of each value, preserving
the order of those last occurrences.
""", """
def remove_dupes_keep_last(seq):
    seq = list(seq)
    seen = set()
    out = []
    for x in reversed(seq):
        if x not in seen:
            seen.add(x)
            out.append(x)
    return list(reversed(out))
""", [
    ('remove_dupes_keep_last([1, 2, 1, 3, 2])', '[1, 3, 2]'),
    ('remove_dupes_keep_last([])', '[]'),
    ('remove_dupes_keep_last(["a", "a"])', "['a']"),
])

task("paired_diffs", "paired_diffs", """
Write paired_diffs(nums) -> list. Return the difference between each value and the one before it.
The result is one shorter than the input, and empty when the input has fewer than two values.
""", """
def paired_diffs(nums):
    nums = list(nums)
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]
""", [
    ('paired_diffs([1, 4, 9, 16])', '[3, 5, 7]'),
    ('paired_diffs([5])', '[]'),
    ('paired_diffs([])', '[]'),
])

task("chunk_by_sign", "chunk_by_sign", """
Write chunk_by_sign(nums) -> list of lists. Group consecutive values by sign, where negative,
zero and positive are three different groups. Each group is a list in original order.
""", """
def chunk_by_sign(nums):
    def kind(x):
        return -1 if x < 0 else (1 if x > 0 else 0)
    out = []
    for x in nums:
        if out and kind(out[-1][0]) == kind(x):
            out[-1].append(x)
        else:
            out.append([x])
    return out
""", [
    ('chunk_by_sign([1, 2, -1, -2, 0, 3])', '[[1, 2], [-1, -2], [0], [3]]'),
    ('chunk_by_sign([])', '[]'),
    ('chunk_by_sign([0, 0])', '[[0, 0]]'),
])

task("running_max", "running_max", """
Write running_max(nums) -> list. Each element is the largest value seen so far. Empty input gives
an empty list.
""", """
def running_max(nums):
    out, best = [], None
    for x in nums:
        best = x if best is None else max(best, x)
        out.append(best)
    return out
""", [
    ('running_max([1, 3, 2, 5])', '[1, 3, 3, 5]'),
    ('running_max([-1, -5])', '[-1, -1]'),
    ('running_max([])', '[]'),
])

TEMPLATE = '''import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import {entry}


class TestCase(unittest.TestCase):
    def test_cases(self):
{cases}


if __name__ == "__main__":
    unittest.main()
'''


def test_body(cases):
    lines = []
    for expr, expected in cases:
        if expected == "ValueError":
            lines.append("        with self.assertRaises(ValueError):")
            lines.append("            %s" % expr)
        else:
            lines.append("        self.assertEqual(%s, %s)" % (expr, expected))
    return "\n".join(lines)


def write_family(name, tasks, note):
    d = ROOT / name
    if d.exists():
        shutil.rmtree(d)
    (d / "tests").mkdir(parents=True)
    meta = {"id": name, "verifier": "unittest", "author": "Empire Labs Pty Ltd",
            "note": note, "tasks": []}
    for t in tasks:
        testfile = "tests/test_%s.py" % t["id"]
        (d / testfile).write_text(TEMPLATE.format(entry=t["entry"], cases=test_body(t["cases"])))
        meta["tasks"].append({"id": t["id"], "entry": t["entry"], "spec": t["spec"],
                              "reference": t["reference"], "tests": testfile, "timeout_s": 30})
    (d / "family.json").write_text(json.dumps(meta, indent=1) + "\n")
    print("%-20s %d tasks" % (name, len(tasks)))


if __name__ == "__main__":
    write_family("list-basics", T, "Ten sequence tasks. Third surface, used for T3.")
