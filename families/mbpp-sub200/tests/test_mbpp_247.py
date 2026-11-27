import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import lps  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert lps("TENS FOR TENS") == 5
        assert lps("CARDIO FOR CARDS") == 7
        assert lps("PART OF THE JOURNEY IS PART") == 9


if __name__ == "__main__":
    unittest.main()
