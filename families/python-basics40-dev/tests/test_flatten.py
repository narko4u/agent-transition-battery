import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import flatten


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([["ab"], ["cd"]]), ['ab', 'cd'])
        self.assertEqual(flatten([(1, 2), [3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
