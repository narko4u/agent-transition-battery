import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_Substrings  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_Substrings('112112') == 6
        assert count_Substrings('111') == 6
        assert count_Substrings('1101112') == 12


if __name__ == "__main__":
    unittest.main()
