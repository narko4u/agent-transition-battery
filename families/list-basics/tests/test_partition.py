import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import partition


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(partition([1, 5, 2, 8], 4), ([1, 2], [5, 8]))
        self.assertEqual(partition([], 1), ([], []))
        self.assertEqual(partition([3], 3), ([], [3]))


if __name__ == "__main__":
    unittest.main()
