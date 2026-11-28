import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import first_non_repeating_character  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert first_non_repeating_character("abcabc") == None
        assert first_non_repeating_character("abc") == "a"
        assert first_non_repeating_character("ababc") == "c"


if __name__ == "__main__":
    unittest.main()
