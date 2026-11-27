import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import next_Perfect_Square  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert next_Perfect_Square(35) == 36
        assert next_Perfect_Square(6) == 9
        assert next_Perfect_Square(9) == 16


if __name__ == "__main__":
    unittest.main()
