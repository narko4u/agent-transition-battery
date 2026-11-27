import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import split_two_parts  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
        assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
        assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])


if __name__ == "__main__":
    unittest.main()
