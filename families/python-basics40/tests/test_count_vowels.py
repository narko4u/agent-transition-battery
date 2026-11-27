import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import count_vowels


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("XYZ"), 0)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
