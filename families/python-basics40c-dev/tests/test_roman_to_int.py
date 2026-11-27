import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import roman_to_int


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(roman_to_int("XIV"), 14)

    def test_case_2(self):
        self.assertEqual(roman_to_int("mcmxciv"), 1994)

    def test_case_3(self):
        self.assertEqual(roman_to_int("III"), 3)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            roman_to_int("")

    def test_case_5(self):
        with self.assertRaises(ValueError):
            roman_to_int("ABC")


if __name__ == "__main__":
    unittest.main()
