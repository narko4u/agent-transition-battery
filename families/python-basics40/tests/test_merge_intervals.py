import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import merge_intervals


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(merge_intervals([[1,3],[2,6],[8,10]]), [[1, 6], [8, 10]])
        self.assertEqual(merge_intervals([[1,2],[2,3]]), [[1, 3]])
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([[5,7],[1,4]]), [[1, 4], [5, 7]])


if __name__ == "__main__":
    unittest.main()
