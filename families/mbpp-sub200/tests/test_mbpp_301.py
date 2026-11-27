import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import dict_depth  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
        assert dict_depth({'a':1, 'b': {'c':'python'}})==2
        assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3


if __name__ == "__main__":
    unittest.main()
