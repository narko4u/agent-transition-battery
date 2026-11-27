import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import cube_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert cube_Sum(2) == 72
        assert cube_Sum(3) == 288
        assert cube_Sum(4) == 800


if __name__ == "__main__":
    unittest.main()
