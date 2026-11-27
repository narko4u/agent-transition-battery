import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import closest_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert closest_num(11) == 10
        assert closest_num(7) == 6
        assert closest_num(12) == 11


if __name__ == "__main__":
    unittest.main()
