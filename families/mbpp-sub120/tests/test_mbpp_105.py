import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count([True,False,True]) == 2
        assert count([False,False]) == 0
        assert count([True,True,True]) == 3


if __name__ == "__main__":
    unittest.main()
