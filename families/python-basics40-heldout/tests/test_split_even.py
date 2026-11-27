import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import split_even


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(split_even([1, 2, 3, 4]), ([2, 4], [1, 3]))
        self.assertEqual(split_even([0, 5]), ([0], [5]))
        self.assertEqual(split_even([]), ([], []))


if __name__ == "__main__":
    unittest.main()
