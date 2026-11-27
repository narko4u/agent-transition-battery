import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import top_k


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(top_k([3,1,4,1,5], 2), [5, 4])
        self.assertEqual(top_k([1,2], 5), [2, 1])
        self.assertEqual(top_k([1,2], 0), [])
        self.assertEqual(top_k([], 3), [])


if __name__ == "__main__":
    unittest.main()
