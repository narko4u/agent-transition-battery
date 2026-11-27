import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_anagram


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_anagram("Listen", "Silent"), True)

    def test_case_2(self):
        self.assertEqual(is_anagram("a", "ab"), False)

    def test_case_3(self):
        self.assertEqual(is_anagram("", ""), True)

    def test_case_4(self):
        self.assertEqual(is_anagram("Dormitory", "dirty room"), True)


if __name__ == "__main__":
    unittest.main()
