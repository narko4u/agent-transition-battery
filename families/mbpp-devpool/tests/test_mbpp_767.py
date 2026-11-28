import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_pairs_count  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_pairs_count([1,1,1,1],2) == 6
        assert get_pairs_count([1,5,7,-1,5],6) == 3
        assert get_pairs_count([1,-2,3],1) == 1
        assert get_pairs_count([-1,-2,3],-3) == 1


if __name__ == "__main__":
    unittest.main()
