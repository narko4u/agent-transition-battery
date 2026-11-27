#!/usr/bin/env python3
"""Build the python-basics40 family, forty tasks, from one catalogue.

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

task("roman_to_int", "roman_to_int", """
Write roman_to_int(text) -> int.
Standard Roman numerals with subtractive pairs. Uppercase or lowercase. Raise ValueError on an
empty string or on any character outside I V X L C D M.
""", """
def roman_to_int(text):
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = str(text).upper()
    if not s:
        raise ValueError(text)
    total = 0
    for i, c in enumerate(s):
        if c not in vals:
            raise ValueError(text)
        v = vals[c]
        if i + 1 < len(s) and vals[s[i + 1]] > v:
            total -= v
        else:
            total += v
    return total
""", [
    ('roman_to_int("XIV")', '14'),
    ('roman_to_int("mcmxciv")', '1994'),
    ('roman_to_int("III")', '3'),
    ('roman_to_int("")', 'ValueError'),
    ('roman_to_int("ABC")', 'ValueError'),
])

task("int_to_roman", "int_to_roman", """
Write int_to_roman(n) -> str for 1 <= n <= 3999. Raise ValueError otherwise, including for
non-integers.
""", """
def int_to_roman(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 1 or n > 3999:
        raise ValueError(n)
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
             (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for v, s in table:
        while n >= v:
            out.append(s)
            n -= v
    return "".join(out)
""", [
    ('int_to_roman(1994)', '"MCMXCIV"'),
    ('int_to_roman(4)', '"IV"'),
    ('int_to_roman(3999)', '"MMMCMXCIX"'),
    ('int_to_roman(0)', 'ValueError'),
    ('int_to_roman(4000)', 'ValueError'),
])

task("flatten", "flatten", """
Write flatten(seq) -> list. Recursively flatten nested lists and tuples, preserving order.
Strings are values, not sequences.
""", """
def flatten(seq):
    out = []
    for x in seq:
        if isinstance(x, (list, tuple)):
            out.extend(flatten(x))
        else:
            out.append(x)
    return out
""", [
    ('flatten([1, [2, [3, 4]], 5])', '[1, 2, 3, 4, 5]'),
    ('flatten([])', '[]'),
    ('flatten([["ab"], ["cd"]])', "['ab', 'cd']"),
    ('flatten([(1, 2), [3]])', '[1, 2, 3]'),
])

task("caesar", "caesar", """
Write caesar(text, k) -> str. Rotate ASCII letters by k positions, keeping case. Leave every
other character alone. k may be negative or larger than 26.
""", """
def caesar(text, k):
    out = []
    for c in str(text):
        if c.isalpha() and c.isascii():
            base = ord("A") if c.isupper() else ord("a")
            out.append(chr((ord(c) - base + k) % 26 + base))
        else:
            out.append(c)
    return "".join(out)
""", [
    ('caesar("abc", 1)', '"bcd"'),
    ('caesar("XYZ", 2)', '"ZAB"'),
    ('caesar("a-b!", 3)', '"d-e!"'),
    ('caesar("abc", -1)', '"zab"'),
])

task("binary_search_index", "binary_search_index", """
Write binary_search_index(sorted_list, target) -> int. Return the index of target in an ascending
list, or -1. Use binary search, not a scan.
""", """
def binary_search_index(sorted_list, target):
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        if sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
""", [
    ('binary_search_index([1, 3, 5, 7], 5)', '2'),
    ('binary_search_index([1, 3, 5, 7], 4)', '-1'),
    ('binary_search_index([], 1)', '-1'),
    ('binary_search_index([2], 2)', '0'),
])

task("count_vowels", "count_vowels", """
Write count_vowels(text) -> int. Count a e i o u, case-insensitive, and nothing else.
""", """
def count_vowels(text):
    return sum(1 for c in str(text).lower() if c in "aeiou")
""", [
    ('count_vowels("Hello")', '2'),
    ('count_vowels("XYZ")', '0'),
    ('count_vowels("AEIOU")', '5'),
    ('count_vowels("")', '0'),
])

task("is_anagram", "is_anagram", """
Write is_anagram(a, b) -> bool. Compare letters and digits only, case-insensitive.
""", """
def is_anagram(a, b):
    def key(s):
        return sorted(c for c in str(s).lower() if c.isalnum())
    return key(a) == key(b)
""", [
    ('is_anagram("Listen", "Silent")', 'True'),
    ('is_anagram("a", "ab")', 'False'),
    ('is_anagram("", "")', 'True'),
    ('is_anagram("Dormitory", "dirty room")', 'True'),
])

task("most_common", "most_common", """
Write most_common(items) -> value. Return the most frequent item. On a tie return the one whose
first occurrence comes earliest. Raise ValueError on an empty sequence.
""", """
def most_common(items):
    items = list(items)
    if not items:
        raise ValueError("empty")
    counts, first = {}, {}
    for i, x in enumerate(items):
        counts[x] = counts.get(x, 0) + 1
        first.setdefault(x, i)
    return max(counts, key=lambda x: (counts[x], -first[x]))
""", [
    ('most_common([1, 2, 2, 3])', '2'),
    ('most_common(["a", "b", "b", "a"])', '"a"'),
    ('most_common([9])', '9'),
    ('most_common([])', 'ValueError'),
])

task("max_subarray_sum", "max_subarray_sum", """
Write max_subarray_sum(nums) -> int. Return the largest sum of a non-empty contiguous slice.
Raise ValueError on an empty list.
""", """
def max_subarray_sum(nums):
    nums = list(nums)
    if not nums:
        raise ValueError("empty")
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
""", [
    ('max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4])', '9'),
    ('max_subarray_sum([-3, -1, -2])', '-1'),
    ('max_subarray_sum([5])', '5'),
    ('max_subarray_sum([])', 'ValueError'),
])

task("transpose", "transpose", """
Write transpose(matrix) -> list of lists. Swap rows and columns. An empty matrix returns [].
Raise ValueError if the rows are ragged.
""", """
def transpose(matrix):
    rows = [list(r) for r in matrix]
    if not rows:
        return []
    if any(len(r) != len(rows[0]) for r in rows):
        raise ValueError("ragged")
    return [list(col) for col in zip(*rows)]
""", [
    ('transpose([[1, 2, 3], [4, 5, 6]])', '[[1, 4], [2, 5], [3, 6]]'),
    ('transpose([])', '[]'),
    ('transpose([[1]])', '[[1]]'),
    ('transpose([[1, 2], [3]])', 'ValueError'),
])

task("valid_brackets", "valid_brackets", """
Write valid_brackets(text) -> bool. True when every bracket in () [] {} is closed in the right
order. Ignore all other characters.
""", """
def valid_brackets(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in str(text):
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack
""", [
    ('valid_brackets("()[]{}")', 'True'),
    ('valid_brackets("(]")', 'False'),
    ('valid_brackets("([{}])")', 'True'),
    ('valid_brackets("")', 'True'),
    ('valid_brackets("(") ', 'False'),
])

task("mode_value", "mode_value", """
Write mode_value(nums) -> number. Return the most frequent value. On a tie return the smallest.
Raise ValueError on an empty sequence.
""", """
def mode_value(nums):
    nums = list(nums)
    if not nums:
        raise ValueError("empty")
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    best = max(counts.values())
    return min(x for x, c in counts.items() if c == best)
""", [
    ('mode_value([1, 2, 2, 3])', '2'),
    ('mode_value([3, 1, 3, 1])', '1'),
    ('mode_value([7])', '7'),
    ('mode_value([])', 'ValueError'),
])

task("sum_digits", "sum_digits", """
Write sum_digits(n) -> int. Sum the decimal digits of the absolute value of an integer.
""", """
def sum_digits(n):
    return sum(int(c) for c in str(abs(int(n))))
""", [
    ('sum_digits(123)', '6'),
    ('sum_digits(-45)', '9'),
    ('sum_digits(0)', '0'),
])

task("snake_case", "snake_case", """
Write snake_case(text) -> str. Lowercase, replace every run of non-alphanumeric characters with a
single underscore, strip leading and trailing underscores.
""", """
import re
def snake_case(text):
    s = re.sub(r"[^a-z0-9]+", "_", str(text).lower())
    return s.strip("_")
""", [
    ('snake_case("Hello, World!")', '"hello_world"'),
    ('snake_case("  A  B ")', '"a_b"'),
    ('snake_case("")', '""'),
    ('snake_case("already_snake")', '"already_snake"'),
])

task("initials", "initials", """
Write initials(name) -> str. Take the first letter of each whitespace-separated word, uppercase
it and join with a dot, ending with a dot. "Ada Lovelace" gives "A.L.".
""", """
def initials(name):
    parts = [p for p in str(name).split() if p]
    return "".join(p[0].upper() + "." for p in parts)
""", [
    ('initials("Ada Lovelace")', '"A.L."'),
    ('initials("grace")', '"G."'),
    ('initials("")', '""'),
])

task("split_even", "split_even", """
Write split_even(nums) -> tuple of two lists. First the even numbers in order, then the odd ones
in order. Treat 0 as even.
""", """
def split_even(nums):
    evens, odds = [], []
    for x in nums:
        (evens if x % 2 == 0 else odds).append(x)
    return evens, odds
""", [
    ('split_even([1, 2, 3, 4])', '([2, 4], [1, 3])'),
    ('split_even([0, 5])', '([0], [5])'),
    ('split_even([])', '([], [])'),
])

task("second_largest", "second_largest", """
Write second_largest(nums) -> int. Return the second largest distinct value. Raise ValueError
when there are fewer than two distinct values.
""", """
def second_largest(nums):
    values = sorted(set(nums))
    if len(values) < 2:
        raise ValueError("need two distinct values")
    return values[-2]
""", [
    ('second_largest([1, 3, 2])', '2'),
    ('second_largest([5, 5, 4])', '4'),
    ('second_largest([7])', 'ValueError'),
    ('second_largest([2, 2, 2])', 'ValueError'),
])

task("cumulative_sum", "cumulative_sum", """
Write cumulative_sum(nums) -> list of ints. Each element is the sum of the input up to that
position.
""", """
def cumulative_sum(nums):
    out, total = [], 0
    for x in nums:
        total += x
        out.append(total)
    return out
""", [
    ('cumulative_sum([1, 2, 3])', '[1, 3, 6]'),
    ('cumulative_sum([-1, 1, -1])', '[-1, 0, -1]'),
    ('cumulative_sum([])', '[]'),
])

task("zip_longest_pad", "zip_longest_pad", """
Write zip_longest_pad(a, b, fill) -> list of tuples. Pair elements by position, padding the
shorter sequence with fill.
""", """
def zip_longest_pad(a, b, fill):
    a, b = list(a), list(b)
    out = []
    for i in range(max(len(a), len(b))):
        out.append((a[i] if i < len(a) else fill, b[i] if i < len(b) else fill))
    return out
""", [
    ('zip_longest_pad([1, 2], [3], 0)', '[(1, 3), (2, 0)]'),
    ('zip_longest_pad([], [1], "x")', "[('x', 1)]"),
    ('zip_longest_pad([], [], 0)', '[]'),
])

task("is_power_of_two", "is_power_of_two", """
Write is_power_of_two(n) -> bool. True for 1, 2, 4, 8 and so on. False for 0 and negatives.
""", """
def is_power_of_two(n):
    return isinstance(n, int) and n > 0 and (n & (n - 1)) == 0
""", [
    ('is_power_of_two(1)', 'True'),
    ('is_power_of_two(64)', 'True'),
    ('is_power_of_two(0)', 'False'),
    ('is_power_of_two(-4)', 'False'),
    ('is_power_of_two(6)', 'False'),
])

task("fizzbuzz_list", "fizzbuzz_list", """
Write fizzbuzz_list(n) -> list of str for 1..n inclusive. Multiples of 3 give "Fizz", of 5 give
"Buzz", of both give "FizzBuzz", otherwise the number as a string.
""", """
def fizzbuzz_list(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out
""", [
    ('fizzbuzz_list(5)', '["1", "2", "Fizz", "4", "Buzz"]'),
    ('fizzbuzz_list(15)[-1]', '"FizzBuzz"'),
    ('fizzbuzz_list(0)', '[]'),
])

task("group_anagrams", "group_anagrams", """
Write group_anagrams(words) -> dict. Key is the letters of the word lowercased and sorted, value
is the sorted list of original words in that group. Empty input gives an empty dict.
""", """
def group_anagrams(words):
    out = {}
    for w in words:
        key = "".join(sorted(str(w).lower()))
        out.setdefault(key, []).append(str(w))
    for key in out:
        out[key].sort()
    return out
""", [
    ('group_anagrams(["eat", "tea", "tan", "ate"])',
     "{'aet': ['ate', 'eat', 'tea'], 'ant': ['tan']}"),
    ('group_anagrams([])', '{}'),
])

task("pairs_sum", "pairs_sum", """
Write pairs_sum(nums, target) -> tuple or None. Return the first pair of indices i < j whose
values add to target, as a tuple. Return None when there is no such pair.
""", """
def pairs_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return (seen[target - x], i)
        seen.setdefault(x, i)
    return None
""", [
    ('pairs_sum([2, 7, 11, 15], 9)', '(0, 1)'),
    ('pairs_sum([1, 2], 10)', 'None'),
    ('pairs_sum([3, 3], 6)', '(0, 1)'),
])

task("compress_ranges", "compress_ranges", """
Write compress_ranges(nums) -> str. Given ascending unique ints, compress consecutive runs as
"a-b" and single values as "a", joined by commas. Empty input gives "".
""", """
def compress_ranges(nums):
    nums = list(nums)
    if not nums:
        return ""
    out, start, prev = [], nums[0], nums[0]
    for x in nums[1:]:
        if x == prev + 1:
            prev = x
            continue
        out.append(str(start) if start == prev else "%d-%d" % (start, prev))
        start = prev = x
    out.append(str(start) if start == prev else "%d-%d" % (start, prev))
    return ",".join(out)
""", [
    ('compress_ranges([1, 2, 3, 5, 7, 8, 9])', '"1-3,5,7-9"'),
    ('compress_ranges([])', '""'),
    ('compress_ranges([4])', '"4"'),
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


DEV_IDS = ["slugify", "parse_duration", "chunk", "clamp", "median", "dedupe", "rotate",
            "is_palindrome", "roman_to_int", "int_to_roman", "flatten", "caesar",
            "binary_search_index", "count_vowels", "is_anagram", "most_common",
            "max_subarray_sum", "transpose", "valid_brackets", "mode_value"]
HELDOUT_IDS = ["human_bytes", "parse_query", "format_cents", "merge_intervals", "word_freq",
               "rle_encode", "rle_decode", "top_k", "sum_digits", "snake_case", "initials",
               "split_even", "second_largest", "cumulative_sum", "zip_longest_pad",
               "is_power_of_two", "fizzbuzz_list", "group_anagrams", "pairs_sum",
               "compress_ranges"]

if __name__ == "__main__":
    by_id = {t["id"]: t for t in T}
    missing = [i for i in DEV_IDS + HELDOUT_IDS if i not in by_id]
    if missing:
        raise SystemExit("unknown ids: %s" % ", ".join(missing))
    if len(by_id) != len(DEV_IDS) + len(HELDOUT_IDS):
        raise SystemExit("catalogue has %d tasks, split names %d" % (len(by_id), len(DEV_IDS) + len(HELDOUT_IDS)))
    write_family("python-basics40", T, "All forty tasks. Use for T1.")
    write_family("python-basics40-dev", [by_id[i] for i in DEV_IDS],
                 "Dev half, twenty tasks. The candidate may learn from these.")
    write_family("python-basics40-heldout", [by_id[i] for i in HELDOUT_IDS],
                 "Held-out half, twenty tasks. The candidate never sees these.")
