import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import recursive_list_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
        assert recursive_list_sum(([7, 10, [15,14],[19,41]]))==106
        assert recursive_list_sum(([10, 20, [30,40],[50,60]]))==210


if __name__ == "__main__":
    unittest.main()
