#!/usr/bin/env python3
"""Build the text-basics family, the transfer target for T2.

Same procedure as python-basics (read a spec, handle the stated edge cases, return a pure
function) on a different surface. Used as family B in a T2 run.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
T = []


def task(tid, entry, spec, ref, cases):
    T.append({"id": tid, "entry": entry, "spec": spec.strip(), "reference": ref.strip(),
              "cases": cases})


task("initials", "initials", """
Write initials(name) -> str.
Split the name on whitespace, take the first character of each part, uppercase it, join the
letters with a full stop and end with a full stop. "Ada Lovelace" is "A.L.". An empty or
whitespace-only name returns "".
""", """
def initials(name):
    parts = str(name).split()
    if not parts:
        return ""
    return "".join(p[0].upper() + "." for p in parts)
""", [
    ('initials("Ada Lovelace")', '"A.L."'),
    ('initials("grace brewster hopper")', '"G.B.H."'),
    ('initials("  ")', '""'),
    ('initials("x")', '"X."'),
])

task("wrap_text", "wrap_text", """
Write wrap_text(text, width) -> list of strings.
Break the text into lines of at most width characters at spaces. Never split a word. A word
longer than width goes on its own line. Collapse runs of spaces to one. Empty or whitespace
text returns [].
""", """
def wrap_text(text, width):
    words = str(text).split()
    if not words:
        return []
    lines, cur = [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines
""", [
    ('wrap_text("the quick brown fox", 10)', "['the quick', 'brown fox']"),
    ('wrap_text("a bb ccc", 3)', "['a', 'bb', 'ccc']"),
    ('wrap_text("   ", 5)', '[]'),
    ('wrap_text("abcdef", 3)', "['abcdef']"),
])

task("csv_field", "csv_field", """
Write csv_field(value) -> str.
If the value contains a comma, a double quote or a newline, return it wrapped in double quotes
with every internal double quote doubled. Otherwise return it unchanged. The value is a string
already.
""", """
def csv_field(value):
    if any(ch in value for ch in [",", '"', "\\n"]):
        return '"' + value.replace('"', '""') + '"'
    return value
""", [
    ('csv_field("plain")', '"plain"'),
    ('csv_field("a,b")', '"\\"a,b\\""'),
    ('csv_field(\'he said "hi"\')', '"\\"he said \\"\\"hi\\"\\"\\""'),
    ('csv_field("a\\nb")', '"\\"a\\nb\\""'),
])

task("pluralise", "pluralise", """
Write pluralise(word) -> str.
If the word ends in s, x, z, ch or sh, add "es". If it ends in a consonant followed by y,
replace the y with "ies". Otherwise add "s". Treat the word case-sensitively.
""", """
def pluralise(word):
    w = str(word)
    if w.endswith(("s", "x", "z", "ch", "sh")):
        return w + "es"
    if len(w) > 1 and w.endswith("y") and w[-2].lower() not in "aeiou":
        return w[:-1] + "ies"
    return w + "s"
""", [
    ('pluralise("cat")', '"cats"'),
    ('pluralise("bus")', '"buses"'),
    ('pluralise("city")', '"cities"'),
    ('pluralise("key")', '"keys"'),
])

task("fold_accents", "fold_accents", """
Write fold_accents(text) -> str.
Return the text with diacritics removed from Latin characters: decompose each character with
Unicode NFD and drop combining marks. Other characters are unchanged.
""", """
import unicodedata
def fold_accents(text):
    return "".join(ch for ch in unicodedata.normalize("NFD", text)
                   if unicodedata.category(ch) != "Mn")
""", [
    ('fold_accents("café")', '"cafe"'),
    ('fold_accents("naïve résumé")', '"naive resume"'),
    ('fold_accents("plain")', '"plain"'),
    ('fold_accents("")', '""'),
])

task("title_case", "title_case", """
Write title_case(text) -> str.
Capitalise the first letter of each word and lowercase the rest, except for these small words
when they are neither first nor last: a, an, the, of, in, on, and, or, for, to, at, by, with.
Everything else keeps normal capitalisation of the first letter.
""", """
SMALL = {"a", "an", "the", "of", "in", "on", "and", "or", "for", "to", "at", "by", "with"}
def title_case(text):
    words = str(text).split()
    out = []
    for i, w in enumerate(words):
        low = w.lower()
        if 0 < i < len(words) - 1 and low in SMALL:
            out.append(low)
        else:
            out.append(low[:1].upper() + low[1:])
    return " ".join(out)
""", [
    ('title_case("the lord of the rings")', '"The Lord of the Rings"'),
    ('title_case("a tale of two cities")', '"A Tale of Two Cities"'),
    ('title_case("WAR AND PEACE")', '"War and Peace"'),
    ('title_case("")', '""'),
])

task("ellipsize", "ellipsize", """
Write ellipsize(text, n) -> str.
If the length of text is at most n, return it unchanged. Otherwise take the first n characters,
remove trailing spaces, append three dots and return that.
""", """
def ellipsize(text, n):
    text = str(text)
    if len(text) <= n:
        return text
    return text[:n].rstrip() + "..."
""", [
    ('ellipsize("hello world", 5)', '"hello..."'),
    ('ellipsize("hi", 5)', '"hi"'),
    ('ellipsize("abc def", 4)', '"abc..."'),
    ('ellipsize("", 3)', '""'),
])

task("parse_kv", "parse_kv", """
Write parse_kv(text) -> dict.
Split on semicolons. Trim spaces around each part and around key and value. Skip empty parts.
Split each part on the first equals sign. A part with no equals sign raises ValueError. A
repeated key keeps the last value. An empty string returns {}.
""", """
def parse_kv(text):
    out = {}
    for part in str(text).split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(part)
        k, _, v = part.partition("=")
        out[k.strip()] = v.strip()
    return out
""", [
    ('parse_kv("a=1; b=2")', "{'a': '1', 'b': '2'}"),
    ('parse_kv("a=1; a=2")', "{'a': '2'}"),
    ('parse_kv("")', "{}"),
    ('parse_kv("a=1; broken")', 'ValueError'),
])

task("caesar", "caesar", """
Write caesar(text, k) -> str.
Shift every ASCII letter forward by k positions, wrapping around the alphabet and preserving
case. Characters that are not ASCII letters are unchanged. k may be negative.
""", """
def caesar(text, k):
    out = []
    for ch in str(text):
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + k) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + k) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)
""", [
    ('caesar("Abc xyz", 2)', '"Cde zab"'),
    ('caesar("abc", -1)', '"zab"'),
    ('caesar("Hello, World!", 0)', '"Hello, World!"'),
    ('caesar("z", 1)', '"a"'),
])

task("anagram_key", "anagram_key", """
Write anagram_key(word) -> str.
Lowercase the word, drop every character that is not an ASCII letter, sort the remaining
characters and return the string.
""", """
def anagram_key(word):
    letters = [c for c in str(word).lower() if "a" <= c <= "z"]
    return "".join(sorted(letters))
""", [
    ('anagram_key("Listen")', '"eilnst"'),
    ('anagram_key("silent")', '"eilnst"'),
    ('anagram_key("a1b!")', '"ab"'),
    ('anagram_key("")', '""'),
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
    print("%-24s %d tasks" % (name, len(tasks)))


if __name__ == "__main__":
    write_family("text-basics", T, "Transfer target for T2. Same procedure, different surface.")
