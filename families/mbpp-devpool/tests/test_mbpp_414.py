import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import overlapping  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
        assert overlapping([1,2,3],[4,5,6]) == False
        assert overlapping([1,4,5],[1,4,5]) == True


if __name__ == "__main__":
    unittest.main()
