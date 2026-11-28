import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_of_nth  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
        assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
        assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11


if __name__ == "__main__":
    unittest.main()
