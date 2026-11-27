import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import rotate


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(rotate([1,2,3,4], 1), [4, 1, 2, 3])

    def test_case_2(self):
        self.assertEqual(rotate([1,2,3,4], -1), [2, 3, 4, 1])

    def test_case_3(self):
        self.assertEqual(rotate([1,2,3], 5), [2, 3, 1])

    def test_case_4(self):
        self.assertEqual(rotate([], 3), [])


if __name__ == "__main__":
    unittest.main()
