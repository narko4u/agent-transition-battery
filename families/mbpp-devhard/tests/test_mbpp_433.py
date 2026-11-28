import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_greater  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_greater([1, 2, 3, 4, 5], 4) == False
        assert check_greater([2, 3, 4, 5, 6], 8) == True
        assert check_greater([9, 7, 4, 8, 6, 1], 11) == True


if __name__ == "__main__":
    unittest.main()
