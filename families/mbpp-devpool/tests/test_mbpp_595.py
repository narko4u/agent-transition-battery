import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import min_Swaps  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert min_Swaps("1101","1110") == 1
        assert min_Swaps("111","000") == "Not Possible"
        assert min_Swaps("111","110") == "Not Possible"


if __name__ == "__main__":
    unittest.main()
