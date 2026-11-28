import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import largest_subset  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
        assert largest_subset([10, 5, 3, 15, 20]) == 3
        assert largest_subset([18, 1, 3, 6, 13, 17]) == 4


if __name__ == "__main__":
    unittest.main()
