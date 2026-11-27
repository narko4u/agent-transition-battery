import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Find_Min_Length  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Find_Min_Length([[1],[1,2]]) == 1
        assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
        assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3


if __name__ == "__main__":
    unittest.main()
