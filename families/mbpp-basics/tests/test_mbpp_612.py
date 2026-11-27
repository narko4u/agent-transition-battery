import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import merge  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
        assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
        assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]


if __name__ == "__main__":
    unittest.main()
