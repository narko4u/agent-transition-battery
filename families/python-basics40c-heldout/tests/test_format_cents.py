import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import format_cents


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(format_cents(123456), "$1,234.56")

    def test_case_2(self):
        self.assertEqual(format_cents(0), "$0.00")

    def test_case_3(self):
        self.assertEqual(format_cents(-123), "-$1.23")

    def test_case_4(self):
        self.assertEqual(format_cents(5), "$0.05")


if __name__ == "__main__":
    unittest.main()
