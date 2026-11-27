import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import chunk_by_sign


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(chunk_by_sign([1, 2, -1, -2, 0, 3]), [[1, 2], [-1, -2], [0], [3]])
        self.assertEqual(chunk_by_sign([]), [])
        self.assertEqual(chunk_by_sign([0, 0]), [[0, 0]])


if __name__ == "__main__":
    unittest.main()
