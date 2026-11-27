import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import frequency  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert frequency([1,2,3], 4) == 0
        assert frequency([1,2,2,3,3,3,4], 3) == 3
        assert frequency([0,1,2,3,1,2], 1) == 2


if __name__ == "__main__":
    unittest.main()
