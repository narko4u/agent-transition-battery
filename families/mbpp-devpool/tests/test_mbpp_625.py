import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import swap_List  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert swap_List([1,2,3]) == [3,2,1]
        assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
        assert swap_List([4,5,6]) == [6,5,4]


if __name__ == "__main__":
    unittest.main()
