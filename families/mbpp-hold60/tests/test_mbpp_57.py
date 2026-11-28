import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Max_Num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Max_Num([1,2,3]) == 321
        assert find_Max_Num([4,5,6,1]) == 6541
        assert find_Max_Num([1,2,3,9]) == 9321


if __name__ == "__main__":
    unittest.main()
