import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_sum([1,2,3,1,1,4,5,6]) == 21
        assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
        assert find_sum([12,10,9,45,2,10,10,45,10]) == 78


if __name__ == "__main__":
    unittest.main()
