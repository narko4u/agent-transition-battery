import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Find_Min  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
        assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
        assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']


if __name__ == "__main__":
    unittest.main()
