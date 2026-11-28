import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_list([10,20,30],[15,25,35])==[25,45,65]
        assert sum_list([1,2,3],[5,6,7])==[6,8,10]
        assert sum_list([15,20,30],[15,45,75])==[30,65,105]


if __name__ == "__main__":
    unittest.main()
