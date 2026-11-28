import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sumofFactors  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sumofFactors(18) == 26
        assert sumofFactors(30) == 48
        assert sumofFactors(6) == 8


if __name__ == "__main__":
    unittest.main()
