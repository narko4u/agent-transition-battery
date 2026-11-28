import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_char  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_char("abba") == "Valid"
        assert check_char("a") == "Valid"
        assert check_char("abcd") == "Invalid"


if __name__ == "__main__":
    unittest.main()
