import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import last  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert last([1,2,3],1) == 0
        assert last([1,1,1,2,3,4],1) == 2
        assert last([2,3,2,3,6,8,9],3) == 3


if __name__ == "__main__":
    unittest.main()
