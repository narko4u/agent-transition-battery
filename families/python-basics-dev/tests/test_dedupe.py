import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import dedupe


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(dedupe([1,2,1,3,2]), [1, 2, 3])
        self.assertEqual(dedupe(["a","a"]), ['a'])
        self.assertEqual(dedupe([[1],[1],[2]]), [[1], [2]])
        self.assertEqual(dedupe([]), [])


if __name__ == "__main__":
    unittest.main()
