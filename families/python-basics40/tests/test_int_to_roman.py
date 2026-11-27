import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import int_to_roman


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(int_to_roman(1994), "MCMXCIV")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")
        with self.assertRaises(ValueError):
            int_to_roman(0)
        with self.assertRaises(ValueError):
            int_to_roman(4000)


if __name__ == "__main__":
    unittest.main()
