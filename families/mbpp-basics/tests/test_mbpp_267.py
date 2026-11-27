import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import square_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert square_Sum(2) == 10
        assert square_Sum(3) == 35
        assert square_Sum(4) == 84


if __name__ == "__main__":
    unittest.main()
