import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import circle_circumference  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
        assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)
        assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
