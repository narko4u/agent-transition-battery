import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import pos_count  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert pos_count([1,-2,3,-4]) == 2
        assert pos_count([3,4,5,-1]) == 3
        assert pos_count([1,2,3,4]) == 4


if __name__ == "__main__":
    unittest.main()
