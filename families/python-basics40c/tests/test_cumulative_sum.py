import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import cumulative_sum


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(cumulative_sum([1, 2, 3]), [1, 3, 6])

    def test_case_2(self):
        self.assertEqual(cumulative_sum([-1, 1, -1]), [-1, 0, -1])

    def test_case_3(self):
        self.assertEqual(cumulative_sum([]), [])


if __name__ == "__main__":
    unittest.main()
