import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import triangle_area  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert triangle_area(-1) == None
        assert triangle_area(0) == 0
        assert triangle_area(2) == 4


if __name__ == "__main__":
    unittest.main()
