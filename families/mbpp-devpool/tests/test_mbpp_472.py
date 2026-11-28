import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_Consecutive  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_Consecutive([1,2,3,4,5]) == True
        assert check_Consecutive([1,2,3,5,6]) == False
        assert check_Consecutive([1,2,1]) == False


if __name__ == "__main__":
    unittest.main()
