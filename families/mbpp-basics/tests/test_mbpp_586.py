import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import split_Arr  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
        assert split_Arr([1,2,3,4],1) == [2,3,4,1]
        assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]


if __name__ == "__main__":
    unittest.main()
