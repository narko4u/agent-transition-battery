import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import volume_cylinder  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
        assert math.isclose(volume_cylinder(4,5), 251.32000000000002, rel_tol=0.001)
        assert math.isclose(volume_cylinder(4,10), 502.64000000000004, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
