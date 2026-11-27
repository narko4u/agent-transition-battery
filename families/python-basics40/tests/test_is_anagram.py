import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_anagram


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_anagram("Listen", "Silent"), True)
        self.assertEqual(is_anagram("a", "ab"), False)
        self.assertEqual(is_anagram("", ""), True)
        self.assertEqual(is_anagram("Dormitory", "dirty room"), True)


if __name__ == "__main__":
    unittest.main()
