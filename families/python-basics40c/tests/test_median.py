import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import median


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(median([3,1,2]), 2.0)

    def test_case_2(self):
        self.assertEqual(median([4,1,3,2]), 2.5)

    def test_case_3(self):
        self.assertEqual(median([7]), 7.0)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            median([])


if __name__ == "__main__":
    unittest.main()
