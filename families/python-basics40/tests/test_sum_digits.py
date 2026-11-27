import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import sum_digits


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(-45), 9)
        self.assertEqual(sum_digits(0), 0)


if __name__ == "__main__":
    unittest.main()
