import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import divisor  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert divisor(15) == 4
        assert divisor(12) == 6
        assert divisor(9) == 3


if __name__ == "__main__":
    unittest.main()
