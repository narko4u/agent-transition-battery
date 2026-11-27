import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import neg_nos  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert neg_nos([-1,4,5,-6]) == [-1,-6]
        assert neg_nos([-1,-2,3,4]) == [-1,-2]
        assert neg_nos([-7,-6,8,9]) == [-7,-6]


if __name__ == "__main__":
    unittest.main()
