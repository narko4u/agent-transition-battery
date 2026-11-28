import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import highest_Power_of_2  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert highest_Power_of_2(10) == 8
        assert highest_Power_of_2(19) == 16
        assert highest_Power_of_2(32) == 32


if __name__ == "__main__":
    unittest.main()
