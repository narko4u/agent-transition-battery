import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_min_diff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_min_diff((1,5,3,19,18,25),6) == 1
        assert find_min_diff((4,3,2,6),4) == 1
        assert find_min_diff((30,5,20,9),4) == 4


if __name__ == "__main__":
    unittest.main()
