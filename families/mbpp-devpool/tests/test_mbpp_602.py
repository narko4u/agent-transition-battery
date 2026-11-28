import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import first_repeated_char  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert first_repeated_char("abcabc") == "a"
        assert first_repeated_char("abc") == None
        assert first_repeated_char("123123") == "1"


if __name__ == "__main__":
    unittest.main()
