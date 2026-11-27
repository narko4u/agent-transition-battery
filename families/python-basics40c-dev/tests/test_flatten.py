import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import flatten


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_case_2(self):
        self.assertEqual(flatten([]), [])

    def test_case_3(self):
        self.assertEqual(flatten([["ab"], ["cd"]]), ['ab', 'cd'])

    def test_case_4(self):
        self.assertEqual(flatten([(1, 2), [3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
