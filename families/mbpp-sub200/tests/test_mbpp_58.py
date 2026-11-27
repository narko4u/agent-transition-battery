import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import opposite_Signs  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert opposite_Signs(1,-2) == True
        assert opposite_Signs(3,2) == False
        assert opposite_Signs(-10,-10) == False
        assert opposite_Signs(-2,2) == True


if __name__ == "__main__":
    unittest.main()
