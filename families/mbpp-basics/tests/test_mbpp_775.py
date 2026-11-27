import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import odd_position  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert odd_position([2,1,4,3,6,7,6,3]) == True
        assert odd_position([4,1,2]) == True
        assert odd_position([1,2,3]) == False


if __name__ == "__main__":
    unittest.main()
