import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import multiply_num  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
        assert math.isclose(multiply_num((-10,-20,-30)), -2000.0, rel_tol=0.001)
        assert math.isclose(multiply_num((19,15,18)), 1710.0, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
