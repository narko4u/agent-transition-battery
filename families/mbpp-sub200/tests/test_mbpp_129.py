import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import magic_square_test  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
        assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
        assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False


if __name__ == "__main__":
    unittest.main()
