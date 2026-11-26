import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import chunk


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(chunk([1,2,3,4,5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunk([], 3), [])
        self.assertEqual(chunk("abcd", 3), [['a', 'b', 'c'], ['d']])
        with self.assertRaises(ValueError):
            chunk([1], 0)


if __name__ == "__main__":
    unittest.main()
