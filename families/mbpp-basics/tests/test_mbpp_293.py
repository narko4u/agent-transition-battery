import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import otherside_rightangle  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert otherside_rightangle(7,8)==10.63014581273465
        assert otherside_rightangle(3,4)==5
        assert otherside_rightangle(7,15)==16.55294535724685


if __name__ == "__main__":
    unittest.main()
