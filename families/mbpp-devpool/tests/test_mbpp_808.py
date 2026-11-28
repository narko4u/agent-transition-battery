import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_K  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_K((10, 4, 5, 6, 8), 6) == True
        assert check_K((1, 2, 3, 4, 5, 6), 7) == False
        assert check_K((7, 8, 9, 44, 11, 12), 11) == True


if __name__ == "__main__":
    unittest.main()
