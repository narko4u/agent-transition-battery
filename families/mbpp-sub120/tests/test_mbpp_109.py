import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import odd_Equivalent  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert odd_Equivalent("011001",6) == 3
        assert odd_Equivalent("11011",5) == 4
        assert odd_Equivalent("1010",4) == 2


if __name__ == "__main__":
    unittest.main()
