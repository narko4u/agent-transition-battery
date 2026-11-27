import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import hexagonal_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert hexagonal_num(10) == 190
        assert hexagonal_num(5) == 45
        assert hexagonal_num(7) == 91


if __name__ == "__main__":
    unittest.main()
