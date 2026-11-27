import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import text_match_wordz_middle  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert text_match_wordz_middle("pythonzabc.")==True
        assert text_match_wordz_middle("zxyabc.")==False
        assert text_match_wordz_middle("  lang  .")==False


if __name__ == "__main__":
    unittest.main()
