import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import binary_search_index


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(binary_search_index([1, 3, 5, 7], 5), 2)
        self.assertEqual(binary_search_index([1, 3, 5, 7], 4), -1)
        self.assertEqual(binary_search_index([], 1), -1)
        self.assertEqual(binary_search_index([2], 2), 0)


if __name__ == "__main__":
    unittest.main()
