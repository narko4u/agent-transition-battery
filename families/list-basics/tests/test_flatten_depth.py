import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import flatten_depth


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(flatten_depth([1, [2, [3, [4]]]], 1), [1, 2, [3, [4]]])
        self.assertEqual(flatten_depth([1, [2, [3, [4]]]], 9), [1, 2, 3, 4])
        self.assertEqual(flatten_depth([1, [2]], 0), [1, [2]])
        with self.assertRaises(ValueError):
            flatten_depth([1], -1)


if __name__ == "__main__":
    unittest.main()
