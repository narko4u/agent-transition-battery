import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Power_Of_Two  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert differ_At_One_Bit_Pos(13,9) == True
        assert differ_At_One_Bit_Pos(15,8) == False
        assert differ_At_One_Bit_Pos(2,4) == False
        assert differ_At_One_Bit_Pos(2, 3) == True
        assert differ_At_One_Bit_Pos(5, 1) == True
        assert differ_At_One_Bit_Pos(1, 5) == True


if __name__ == "__main__":
    unittest.main()
