import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_smaller  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_smaller((1, 2, 3), (2, 3, 4)) == False
        assert check_smaller((4, 5, 6), (3, 4, 5)) == True
        assert check_smaller((11, 12, 13), (10, 11, 12)) == True


if __name__ == "__main__":
    unittest.main()
