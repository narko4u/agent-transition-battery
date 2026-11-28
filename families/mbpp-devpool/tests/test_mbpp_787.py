import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import text_match_three  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert not text_match_three("ac")
        assert not text_match_three("dc")
        assert text_match_three("abbbba")
        assert text_match_three("caacabbbba")


if __name__ == "__main__":
    unittest.main()
