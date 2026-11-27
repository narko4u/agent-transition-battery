import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Find_Max  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
        assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
        assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]


if __name__ == "__main__":
    unittest.main()
