import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3
        assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3
        assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1


if __name__ == "__main__":
    unittest.main()
