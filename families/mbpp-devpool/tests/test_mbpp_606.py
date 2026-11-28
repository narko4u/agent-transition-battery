import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import radian_degree  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert radian_degree(90)==1.5707963267948966
        assert radian_degree(60)==1.0471975511965976
        assert radian_degree(120)==2.0943951023931953


if __name__ == "__main__":
    unittest.main()
