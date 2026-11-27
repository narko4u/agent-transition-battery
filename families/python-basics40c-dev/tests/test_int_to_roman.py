import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import int_to_roman


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(int_to_roman(1994), "MCMXCIV")

    def test_case_2(self):
        self.assertEqual(int_to_roman(4), "IV")

    def test_case_3(self):
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_case_4(self):
        with self.assertRaises(ValueError):
            int_to_roman(0)

    def test_case_5(self):
        with self.assertRaises(ValueError):
            int_to_roman(4000)


if __name__ == "__main__":
    unittest.main()
