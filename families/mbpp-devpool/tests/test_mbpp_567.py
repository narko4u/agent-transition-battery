import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import issort_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
        assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False
        assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False


if __name__ == "__main__":
    unittest.main()
