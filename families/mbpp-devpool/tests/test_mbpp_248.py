import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import harmonic_sum  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
        assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
        assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
