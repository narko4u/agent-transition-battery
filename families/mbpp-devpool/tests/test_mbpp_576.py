import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Sub_Array  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_Sub_Array([1,4,3,5],[1,2]) == False
        assert is_Sub_Array([1,2,1],[1,2,1]) == True
        assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False


if __name__ == "__main__":
    unittest.main()
