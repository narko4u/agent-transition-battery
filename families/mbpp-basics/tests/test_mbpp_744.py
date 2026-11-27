import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_none  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_none((10, 4, 5, 6, None)) == True
        assert check_none((7, 8, 9, 11, 14)) == False
        assert check_none((1, 2, 3, 4, None)) == True


if __name__ == "__main__":
    unittest.main()
