import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import paired_diffs


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(paired_diffs([1, 4, 9, 16]), [3, 5, 7])
        self.assertEqual(paired_diffs([5]), [])
        self.assertEqual(paired_diffs([]), [])


if __name__ == "__main__":
    unittest.main()
