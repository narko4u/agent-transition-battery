import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import move_zero  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
        assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
        assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]


if __name__ == "__main__":
    unittest.main()
