import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sub_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
        assert sub_list([1,2],[3,4])==[-2,-2]
        assert sub_list([90,120],[50,70])==[40,50]


if __name__ == "__main__":
    unittest.main()
