import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Extract  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
        assert Extract([[1,2,3],[4, 5]]) == [1,4]
        assert Extract([[9,8,1],[1,2]]) == [9,1]


if __name__ == "__main__":
    unittest.main()
