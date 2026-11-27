import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import ascii_value  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert ascii_value('A')==65
        assert ascii_value('R')==82
        assert ascii_value('S')==83


if __name__ == "__main__":
    unittest.main()
