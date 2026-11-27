import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_binary_seq  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
        assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
        assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
