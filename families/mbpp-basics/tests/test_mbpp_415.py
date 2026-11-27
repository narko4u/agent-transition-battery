import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_Product  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
        assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
        assert max_Product([1,2,3]) == (2,3)


if __name__ == "__main__":
    unittest.main()
