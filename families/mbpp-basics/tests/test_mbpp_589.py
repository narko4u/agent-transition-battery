import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import perfect_squares  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
        assert perfect_squares(50,100)==[64, 81, 100]
        assert perfect_squares(100,200)==[100, 121, 144, 169, 196]


if __name__ == "__main__":
    unittest.main()
