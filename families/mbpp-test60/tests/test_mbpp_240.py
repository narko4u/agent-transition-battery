import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import replace_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
        assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
        assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]


if __name__ == "__main__":
    unittest.main()
