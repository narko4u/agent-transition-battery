import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import volume_cone  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
        assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)
        assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
