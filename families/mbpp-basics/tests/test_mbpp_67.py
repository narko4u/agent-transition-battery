import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import bell_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert bell_number(2)==2
        assert bell_number(10)==115975
        assert bell_number(56)==6775685320645824322581483068371419745979053216268760300


if __name__ == "__main__":
    unittest.main()
