import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Diff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
        assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
        assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]


if __name__ == "__main__":
    unittest.main()
