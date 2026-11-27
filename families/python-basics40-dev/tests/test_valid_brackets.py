import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import valid_brackets


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(valid_brackets("()[]{}"), True)
        self.assertEqual(valid_brackets("(]"), False)
        self.assertEqual(valid_brackets("([{}])"), True)
        self.assertEqual(valid_brackets(""), True)
        self.assertEqual(valid_brackets("(") , False)


if __name__ == "__main__":
    unittest.main()
