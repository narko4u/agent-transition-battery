import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import dedupe_adjacent


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(dedupe_adjacent([1, 1, 2, 3, 3, 3, 2]), [1, 2, 3, 2])
        self.assertEqual(dedupe_adjacent([]), [])
        self.assertEqual(dedupe_adjacent(["a"]), ['a'])


if __name__ == "__main__":
    unittest.main()
