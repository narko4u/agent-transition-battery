import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import and_tuples  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
        assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
        assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)


if __name__ == "__main__":
    unittest.main()
