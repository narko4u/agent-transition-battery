import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import sum_digits


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_digits(123), 6)

    def test_case_2(self):
        self.assertEqual(sum_digits(-45), 9)

    def test_case_3(self):
        self.assertEqual(sum_digits(0), 0)


if __name__ == "__main__":
    unittest.main()
