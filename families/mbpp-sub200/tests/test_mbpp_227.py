import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import min_of_three  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert min_of_three(10,20,0)==0
        assert min_of_three(19,15,18)==15
        assert min_of_three(-10,-20,-30)==-30


if __name__ == "__main__":
    unittest.main()
