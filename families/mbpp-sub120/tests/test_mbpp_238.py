import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import number_of_substrings  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert number_of_substrings("abc") == 6
        assert number_of_substrings("abcd") == 10
        assert number_of_substrings("abcde") == 15


if __name__ == "__main__":
    unittest.main()
