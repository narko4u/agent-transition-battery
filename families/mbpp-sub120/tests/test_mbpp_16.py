import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import text_lowercase_underscore  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert text_lowercase_underscore("aab_cbbbc")==(True)
        assert text_lowercase_underscore("aab_Abbbc")==(False)
        assert text_lowercase_underscore("Aaab_abbbc")==(False)


if __name__ == "__main__":
    unittest.main()
