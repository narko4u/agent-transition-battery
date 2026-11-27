import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Volume  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Volume(10,8,6) == 240
        assert find_Volume(3,2,2) == 6
        assert find_Volume(1,2,1) == 1


if __name__ == "__main__":
    unittest.main()
