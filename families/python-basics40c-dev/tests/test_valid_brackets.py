import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import valid_brackets


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(valid_brackets("()[]{}"), True)

    def test_case_2(self):
        self.assertEqual(valid_brackets("(]"), False)

    def test_case_3(self):
        self.assertEqual(valid_brackets("([{}])"), True)

    def test_case_4(self):
        self.assertEqual(valid_brackets(""), True)

    def test_case_5(self):
        self.assertEqual(valid_brackets("(") , False)


if __name__ == "__main__":
    unittest.main()
