import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import wrap_text


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(wrap_text("the quick brown fox", 10), ['the quick', 'brown fox'])
        self.assertEqual(wrap_text("a bb ccc", 3), ['a', 'bb', 'ccc'])
        self.assertEqual(wrap_text("   ", 5), [])
        self.assertEqual(wrap_text("abcdef", 3), ['abcdef'])


if __name__ == "__main__":
    unittest.main()
