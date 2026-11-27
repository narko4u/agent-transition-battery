import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import largest_neg  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert largest_neg([1,2,3,-4,-6]) == -6
        assert largest_neg([1,2,3,-8,-9]) == -9
        assert largest_neg([1,2,3,4,-1]) == -1


if __name__ == "__main__":
    unittest.main()
