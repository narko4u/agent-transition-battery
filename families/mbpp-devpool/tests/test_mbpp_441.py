import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import surfacearea_cube  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert surfacearea_cube(5)==150
        assert surfacearea_cube(3)==54
        assert surfacearea_cube(10)==600


if __name__ == "__main__":
    unittest.main()
