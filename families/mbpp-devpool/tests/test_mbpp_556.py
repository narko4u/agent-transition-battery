import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Odd_Pair  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Odd_Pair([5,4,7,2,1],5) == 6
        assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
        assert find_Odd_Pair([1,2,3],3) == 2


if __name__ == "__main__":
    unittest.main()
