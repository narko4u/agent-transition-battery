import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import pairs_sum


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(pairs_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(pairs_sum([1, 2], 10), None)
        self.assertEqual(pairs_sum([3, 3], 6), (0, 1))


if __name__ == "__main__":
    unittest.main()
