import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import running_max


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(running_max([1, 3, 2, 5]), [1, 3, 3, 5])
        self.assertEqual(running_max([-1, -5]), [-1, -1])
        self.assertEqual(running_max([]), [])


if __name__ == "__main__":
    unittest.main()
