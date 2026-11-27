import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_Abs_Diff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_Abs_Diff((2,1,5,3)) == 4
        assert max_Abs_Diff((9,3,2,5,1)) == 8
        assert max_Abs_Diff((3,2,1)) == 2


if __name__ == "__main__":
    unittest.main()
