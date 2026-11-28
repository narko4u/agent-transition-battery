import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import intersection_array  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
        assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
        assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]


if __name__ == "__main__":
    unittest.main()
