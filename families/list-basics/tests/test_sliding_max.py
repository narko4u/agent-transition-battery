import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import sliding_max


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(sliding_max([1, 3, 2, 5, 4], 2), [3, 3, 5, 5])
        self.assertEqual(sliding_max([5], 1), [5])
        with self.assertRaises(ValueError):
            sliding_max([1, 2], 3)
        with self.assertRaises(ValueError):
            sliding_max([1, 2], 0)


if __name__ == "__main__":
    unittest.main()
