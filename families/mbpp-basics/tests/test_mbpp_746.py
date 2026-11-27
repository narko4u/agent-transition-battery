import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sector_area  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sector_area(4,45)==6.283185307179586
        assert sector_area(9,45)==31.808625617596654
        assert sector_area(9,361)==None


if __name__ == "__main__":
    unittest.main()
