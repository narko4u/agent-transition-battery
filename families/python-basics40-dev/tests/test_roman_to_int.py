import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import roman_to_int


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(roman_to_int("XIV"), 14)
        self.assertEqual(roman_to_int("mcmxciv"), 1994)
        self.assertEqual(roman_to_int("III"), 3)
        with self.assertRaises(ValueError):
            roman_to_int("")
        with self.assertRaises(ValueError):
            roman_to_int("ABC")


if __name__ == "__main__":
    unittest.main()
