import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_majority  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
        assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
        assert is_majority([1, 1, 1, 2, 2], 5, 1) == True
        assert is_majority([1, 1, 2, 2], 5, 1) == False


if __name__ == "__main__":
    unittest.main()
