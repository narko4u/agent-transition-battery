import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import volume_sphere  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
        assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=0.001)
        assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
