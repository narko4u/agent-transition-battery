import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_polite  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_polite(7) == 11
        assert is_polite(4) == 7
        assert is_polite(9) == 13


if __name__ == "__main__":
    unittest.main()
