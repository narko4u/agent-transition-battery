import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import compress_ranges


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(compress_ranges([1, 2, 3, 5, 7, 8, 9]), "1-3,5,7-9")

    def test_case_2(self):
        self.assertEqual(compress_ranges([]), "")

    def test_case_3(self):
        self.assertEqual(compress_ranges([4]), "4")


if __name__ == "__main__":
    unittest.main()
