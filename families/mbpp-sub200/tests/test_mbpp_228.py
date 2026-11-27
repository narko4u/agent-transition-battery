import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import all_Bits_Set_In_The_Given_Range  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
        assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
        assert all_Bits_Set_In_The_Given_Range(39,4,6) == False


if __name__ == "__main__":
    unittest.main()
