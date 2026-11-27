import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import dedupe


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(dedupe([1,2,1,3,2]), [1, 2, 3])

    def test_case_2(self):
        self.assertEqual(dedupe(["a","a"]), ['a'])

    def test_case_3(self):
        self.assertEqual(dedupe([[1],[1],[2]]), [[1], [2]])

    def test_case_4(self):
        self.assertEqual(dedupe([]), [])


if __name__ == "__main__":
    unittest.main()
