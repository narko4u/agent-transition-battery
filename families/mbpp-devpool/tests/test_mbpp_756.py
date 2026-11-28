import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import text_match_zero_one  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert text_match_zero_one("ac")==False
        assert text_match_zero_one("dc")==False
        assert text_match_zero_one("abbbba")==True
        assert text_match_zero_one("dsabbbba")==True
        assert text_match_zero_one("asbbbba")==False
        assert text_match_zero_one("abaaa")==True


if __name__ == "__main__":
    unittest.main()
