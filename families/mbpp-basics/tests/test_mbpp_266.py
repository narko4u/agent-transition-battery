import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import lateralsurface_cube  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert lateralsurface_cube(5)==100
        assert lateralsurface_cube(9)==324
        assert lateralsurface_cube(10)==400


if __name__ == "__main__":
    unittest.main()
