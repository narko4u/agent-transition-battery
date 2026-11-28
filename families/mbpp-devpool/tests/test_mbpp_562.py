import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Find_Max_Length  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
        assert Find_Max_Length([[0,1],[2,2,],[3,2,1]]) == 3
        assert Find_Max_Length([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5


if __name__ == "__main__":
    unittest.main()
