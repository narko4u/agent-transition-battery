import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import babylonian_squareroot  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
        assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=0.001)
        assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
