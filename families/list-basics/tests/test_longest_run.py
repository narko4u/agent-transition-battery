import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import longest_run


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(longest_run([1, 1, 2, 3, 3, 3]), 3)
        self.assertEqual(longest_run([]), 0)
        self.assertEqual(longest_run([4]), 1)
        self.assertEqual(longest_run([1, 2, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()
