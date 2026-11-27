import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import square_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert square_Sum(2) == 20
        assert square_Sum(3) == 56
        assert square_Sum(4) == 120


if __name__ == "__main__":
    unittest.main()
