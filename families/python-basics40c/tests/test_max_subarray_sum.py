import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import max_subarray_sum


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]), 9)

    def test_case_2(self):
        self.assertEqual(max_subarray_sum([-3, -1, -2]), -1)

    def test_case_3(self):
        self.assertEqual(max_subarray_sum([5]), 5)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            max_subarray_sum([])


if __name__ == "__main__":
    unittest.main()
