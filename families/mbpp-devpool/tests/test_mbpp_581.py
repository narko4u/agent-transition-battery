import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import surface_Area  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert surface_Area(3,4) == 33
        assert surface_Area(4,5) == 56
        assert surface_Area(1,2) == 5


if __name__ == "__main__":
    unittest.main()
