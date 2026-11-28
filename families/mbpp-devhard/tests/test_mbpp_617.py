import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import min_Jumps  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert min_Jumps((3,4),11)==3.5
        assert min_Jumps((3,4),0)==0
        assert min_Jumps((11,14),11)==1


if __name__ == "__main__":
    unittest.main()
