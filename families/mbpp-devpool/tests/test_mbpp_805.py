import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_sum_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
        assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
        assert max_sum_list([[2,3,1]])==[2,3,1]


if __name__ == "__main__":
    unittest.main()
