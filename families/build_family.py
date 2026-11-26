#!/usr/bin/env python3
"""Build the python-basics family from one catalogue.

Emits families/python-basics (all tasks), python-basics-dev (first 8) and
python-basics-heldout (last 8), each with its own tests directory so the verifier
hash is independent. A reference solution is stored per task; the scripted
adapter uses it, the deepseek adapter never sees it.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent

T = []


def task(tid, entry, spec, ref, cases):
    T.append({"id": tid, "entry": entry, "spec": spec.strip(), "reference": ref.strip(),
              "cases": cases})


task("slugify", "slugify", """
Write slugify(text) -> str.
Lowercase. Replace every run of characters that are not ASCII letters or digits with a single
hyphen. Strip leading and trailing hyphens. Return "" when nothing remains.
""", """
import re
def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower())
    return s.strip("-")
""", [
    ('slugify("Hello, World!")', '"hello-world"'),
    ('slugify("  A  B  ")', '"a-b"'),
    ('slugify("Café Olé")', '"caf-ol"'),
    ('slugify("!!!")', '""'),
])

task("parse_duration", "parse_duration", """
Write parse_duration(text) -> int seconds.
Accept an optional sequence of <int><unit> where unit is h, m or s, in that order, each at most
once. "1h30m45s" is 5445. "90s" is 90. "2m" is 120. An empty string is 0. Any other form,
including a bad unit or a repeated unit, raises ValueError.
""", """
import re
def parse_duration(text):
    text = str(text).strip()
    if text == "":
        return 0
    m = re.fullmatch(r"(?:(\\d+)h)?(?:(\\d+)m)?(?:(\\d+)s)?", text)
    if not m or not any(m.groups()):
        raise ValueError(text)
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s
""", [
    ('parse_duration("1h30m45s")', '5445'),
    ('parse_duration("90s")', '90'),
    ('parse_duration("2m")', '120'),
    ('parse_duration("")', '0'),
    ('parse_duration("1x")', 'ValueError'),
])

task("chunk", "chunk", """
Write chunk(seq, n) -> list of lists.
Split seq into consecutive lists of length n, the last one shorter if needed. n must be a
positive int, otherwise raise ValueError. chunk([], 3) is [].
""", """
def chunk(seq, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError(n)
    seq = list(seq)
    return [seq[i:i + n] for i in range(0, len(seq), n)]
""", [
    ('chunk([1,2,3,4,5], 2)', '[[1, 2], [3, 4], [5]]'),
    ('chunk([], 3)', '[]'),
    ('chunk("abcd", 3)', "[['a', 'b', 'c'], ['d']]"),
    ('chunk([1], 0)', 'ValueError'),
])

task("clamp", "clamp", """
Write clamp(x, lo, hi) -> number.
Return x limited to the inclusive range [lo, hi]. Raise ValueError when lo > hi.
""", """
def clamp(x, lo, hi):
    if lo > hi:
        raise ValueError((lo, hi))
    return max(lo, min(hi, x))
""", [
    ('clamp(5, 1, 10)', '5'),
    ('clamp(-5, 1, 10)', '1'),
    ('clamp(50, 1, 10)', '10'),
    ('clamp(1, 5, 2)', 'ValueError'),
])

task("median", "median", """
Write median(nums) -> float.
Return the median of a non-empty sequence of numbers. An even length returns the mean of the two
middle values as a float. An empty sequence raises ValueError.
""", """
def median(nums):
    nums = sorted(nums)
    if not nums:
        raise ValueError("empty")
    n = len(nums)
    mid = n // 2
    if n % 2:
        return float(nums[mid])
    return (nums[mid - 1] + nums[mid]) / 2.0
""", [
    ('median([3,1,2])', '2.0'),
    ('median([4,1,3,2])', '2.5'),
    ('median([7])', '7.0'),
    ('median([])', 'ValueError'),
])

task("dedupe", "dedupe", """
Write dedupe(items) -> list.
Keep the first occurrence of each item, preserving order. Works for unhashable items too, so
use equality rather than a set.
""", """
def dedupe(items):
    out = []
    for x in items:
        if x not in out:
            out.append(x)
    return out
""", [
    ('dedupe([1,2,1,3,2])', '[1, 2, 3]'),
    ('dedupe(["a","a"])', "['a']"),
    ('dedupe([[1],[1],[2]])', '[[1], [2]]'),
    ('dedupe([])', '[]'),
])

task("rotate", "rotate", """
Write rotate(items, k) -> list.
Rotate the sequence right by k places. A negative k rotates left. k may exceed the length.
An empty sequence returns [].
""", """
def rotate(items, k):
    items = list(items)
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items
""", [
    ('rotate([1,2,3,4], 1)', '[4, 1, 2, 3]'),
    ('rotate([1,2,3,4], -1)', '[2, 3, 4, 1]'),
    ('rotate([1,2,3], 5)', '[2, 3, 1]'),
    ('rotate([], 3)', '[]'),
])

task("is_palindrome", "is_palindrome", """
Write is_palindrome(text) -> bool.
Ignore case and every character that is not an ASCII letter or digit. An empty result is True.
""", """
import re
def is_palindrome(text):
    s = re.sub(r"[^a-z0-9]", "", str(text).lower())
    return s == s[::-1]
""", [
    ('is_palindrome("A man, a plan, a canal: Panama")', 'True'),
    ('is_palindrome("abc")', 'False'),
    ('is_palindrome("")', 'True'),
    ('is_palindrome("Never odd or even")', 'True'),
])

task("human_bytes", "human_bytes", """
Write human_bytes(n) -> str.
Below 1000 return "<n> B". Otherwise use KB, MB or GB at 1000 steps, one decimal place, and drop
a trailing ".0". 1000 is "1 KB". 1500 is "1.5 KB". 1000000 is "1 MB".
""", """
def human_bytes(n):
    if n < 1000:
        return "%d B" % n
    for unit in ("KB", "MB", "GB", "TB"):
        n /= 1000.0
        if n < 1000 or unit == "TB":
            s = ("%.1f" % n).rstrip("0").rstrip(".")
            return "%s %s" % (s, unit)
""", [
    ('human_bytes(999)', '"999 B"'),
    ('human_bytes(1000)', '"1 KB"'),
    ('human_bytes(1500)', '"1.5 KB"'),
    ('human_bytes(1000000)', '"1 MB"'),
])

task("parse_query", "parse_query", """
Write parse_query(qs) -> dict.
Split on "&", then on the first "=". A missing value is "". A repeated key keeps the last value.
A plus becomes a space. An empty string returns {}.
""", """
def parse_query(qs):
    out = {}
    if not qs:
        return out
    for part in qs.split("&"):
        if part == "":
            continue
        k, _, v = part.partition("=")
        out[k.replace("+", " ")] = v.replace("+", " ")
    return out
""", [
    ('parse_query("a=1&b=2&a=3")', "{'a': '3', 'b': '2'}"),
    ('parse_query("q=hello+world")', "{'q': 'hello world'}"),
    ('parse_query("flag")', "{'flag': ''}"),
    ('parse_query("")', "{}"),
])

task("format_cents", "format_cents", """
Write format_cents(c) -> str.
Format an integer number of cents as dollars with two decimals and commas in the whole part.
123456 is "$1,234.56". Zero is "$0.00". A negative value puts the minus before the dollar sign:
-123 is "-$1.23".
""", """
def format_cents(c):
    sign = "-" if c < 0 else ""
    c = abs(int(c))
    return "%s$%s.%02d" % (sign, format(c // 100, ","), c % 100)
""", [
    ('format_cents(123456)', '"$1,234.56"'),
    ('format_cents(0)', '"$0.00"'),
    ('format_cents(-123)', '"-$1.23"'),
    ('format_cents(5)', '"$0.05"'),
])

task("merge_intervals", "merge_intervals", """
Write merge_intervals(intervals) -> list.
Each interval is a two-item sequence [start, end] with start <= end. Merge overlapping and
touching intervals and return them sorted by start. [[1,3],[2,6],[8,10]] gives [[1,6],[8,10]].
[[1,2],[2,3]] gives [[1,3]]. An empty list gives [].
""", """
def merge_intervals(intervals):
    out = []
    for s, e in sorted([list(x) for x in intervals]):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
""", [
    ('merge_intervals([[1,3],[2,6],[8,10]])', '[[1, 6], [8, 10]]'),
    ('merge_intervals([[1,2],[2,3]])', '[[1, 3]]'),
    ('merge_intervals([])', '[]'),
    ('merge_intervals([[5,7],[1,4]])', '[[1, 4], [5, 7]]'),
])

task("word_freq", "word_freq", """
Write word_freq(text, n) -> list of (word, count).
Lowercase the text and split on every run of characters that are not ASCII letters. Ignore
empty strings. Sort by count descending, then word ascending. Return at most n pairs. n <= 0
returns [].
""", """
import re
def word_freq(text, n):
    if n <= 0:
        return []
    words = re.findall(r"[a-z]+", str(text).lower())
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
""", [
    ('word_freq("The cat the dog", 2)', "[('the', 2), ('cat', 1)]"),
    ('word_freq("b a b a c", 3)', "[('a', 2), ('b', 2), ('c', 1)]"),
    ('word_freq("", 5)', '[]'),
    ('word_freq("a", 0)', '[]'),
])

task("rle_encode", "rle_encode", """
Write rle_encode(s) -> str.
Run-length encode: each run of one character becomes the character followed by its decimal
count, including runs of length one. "aaabb" is "a3b2". "" is "".
""", """
def rle_encode(s):
    if not s:
        return ""
    out = []
    prev = s[0]
    n = 1
    for ch in s[1:]:
        if ch == prev:
            n += 1
        else:
            out.append("%s%d" % (prev, n))
            prev, n = ch, 1
    out.append("%s%d" % (prev, n))
    return "".join(out)
""", [
    ('rle_encode("aaabb")', '"a3b2"'),
    ('rle_encode("abc")', '"a1b1c1"'),
    ('rle_encode("")', '""'),
    ('rle_encode("a")', '"a1"'),
])

task("rle_decode", "rle_decode", """
Write rle_decode(s) -> str.
Inverse of rle_encode. A letter followed by a positive decimal count repeats the letter that
many times. "a3b2" is "aaabb". "" is "". A malformed string, including a missing count or a
count of zero, raises ValueError.
""", """
import re
def rle_decode(s):
    if s == "":
        return ""
    parts = re.findall(r"([A-Za-z])(\\d+)", s)
    if "".join(a + b for a, b in parts) != s:
        raise ValueError(s)
    out = []
    for ch, num in parts:
        n = int(num)
        if n <= 0:
            raise ValueError(s)
        out.append(ch * n)
    return "".join(out)
""", [
    ('rle_decode("a3b2")', '"aaabb"'),
    ('rle_decode("")', '""'),
    ('rle_decode("a1")', '"a"'),
    ('rle_decode("a0")', 'ValueError'),
])

task("top_k", "top_k", """
Write top_k(nums, k) -> list.
Return the k largest numbers in descending order. k <= 0 returns []. If k exceeds the length,
return every number sorted descending.
""", """
def top_k(nums, k):
    if k <= 0:
        return []
    return sorted(nums, reverse=True)[:k]
""", [
    ('top_k([3,1,4,1,5], 2)', '[5, 4]'),
    ('top_k([1,2], 5)', '[2, 1]'),
    ('top_k([1,2], 0)', '[]'),
    ('top_k([], 3)', '[]'),
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
    print("%-28s %d tasks" % (name, len(tasks)))


if __name__ == "__main__":
    write_family("python-basics", T, "All sixteen tasks. Use for T1.")
    write_family("python-basics-dev", T[:8], "Dev half. The candidate may learn from these.")
    write_family("python-basics-heldout", T[8:], "Held-out half. The candidate never sees these.")
