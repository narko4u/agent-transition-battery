import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import lateralsuface_cylinder  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
        assert math.isclose(lateralsuface_cylinder(4,5), 125.66000000000001, rel_tol=0.001)
        assert math.isclose(lateralsuface_cylinder(4,10), 251.32000000000002, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
