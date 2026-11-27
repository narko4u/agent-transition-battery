import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import surfacearea_sphere  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
        assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=0.001)
        assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
