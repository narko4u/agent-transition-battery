import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_Set_Bits  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_Set_Bits(2) == 1
        assert count_Set_Bits(4) == 1
        assert count_Set_Bits(6) == 2


if __name__ == "__main__":
    unittest.main()
