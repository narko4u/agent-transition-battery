import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import big_diff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert big_diff([1,2,3,4]) == 3
        assert big_diff([4,5,12]) == 8
        assert big_diff([9,2,3]) == 7


if __name__ == "__main__":
    unittest.main()
