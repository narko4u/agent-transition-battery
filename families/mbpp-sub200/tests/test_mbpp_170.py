import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_range_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29
        assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16
        assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38


if __name__ == "__main__":
    unittest.main()
