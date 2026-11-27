import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import count_vowels


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_vowels("Hello"), 2)

    def test_case_2(self):
        self.assertEqual(count_vowels("XYZ"), 0)

    def test_case_3(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_case_4(self):
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
