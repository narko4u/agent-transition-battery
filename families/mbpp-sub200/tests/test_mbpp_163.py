import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import area_polygon  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
        assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
        assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
