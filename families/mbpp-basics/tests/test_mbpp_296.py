import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_Inv_Count  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_Inv_Count([1,20,6,4,5]) == 5
        assert get_Inv_Count([1,2,1]) == 1
        assert get_Inv_Count([1,2,5,6,1]) == 3


if __name__ == "__main__":
    unittest.main()
