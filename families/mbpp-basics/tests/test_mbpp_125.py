import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_length  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_length("11000010001") == 6
        assert find_length("10111") == 1
        assert find_length("11011101100101") == 2


if __name__ == "__main__":
    unittest.main()
