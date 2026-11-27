import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import compress_ranges


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(compress_ranges([1, 2, 3, 5, 7, 8, 9]), "1-3,5,7-9")
        self.assertEqual(compress_ranges([]), "")
        self.assertEqual(compress_ranges([4]), "4")


if __name__ == "__main__":
    unittest.main()
