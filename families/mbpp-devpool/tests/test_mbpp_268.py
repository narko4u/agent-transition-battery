import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_star_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_star_num(3) == 37
        assert find_star_num(4) == 73
        assert find_star_num(5) == 121


if __name__ == "__main__":
    unittest.main()
