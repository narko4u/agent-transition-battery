import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import text_starta_endb  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert text_starta_endb("aabbbb")
        assert not text_starta_endb("aabAbbbc")
        assert not text_starta_endb("accddbbjjj")


if __name__ == "__main__":
    unittest.main()
