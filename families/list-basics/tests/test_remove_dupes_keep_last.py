import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import remove_dupes_keep_last


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(remove_dupes_keep_last([1, 2, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(remove_dupes_keep_last([]), [])
        self.assertEqual(remove_dupes_keep_last(["a", "a"]), ['a'])


if __name__ == "__main__":
    unittest.main()
