import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import zip_longest_pad


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(zip_longest_pad([1, 2], [3], 0), [(1, 3), (2, 0)])
        self.assertEqual(zip_longest_pad([], [1], "x"), [('x', 1)])
        self.assertEqual(zip_longest_pad([], [], 0), [])


if __name__ == "__main__":
    unittest.main()
