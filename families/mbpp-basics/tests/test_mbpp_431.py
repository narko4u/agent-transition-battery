import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import common_element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
        assert common_element([1,2,3,4,5], [6,7,8,9])==None
        assert common_element(['a','b','c'], ['d','b','e'])==True


if __name__ == "__main__":
    unittest.main()
