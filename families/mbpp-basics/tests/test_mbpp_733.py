import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_first_occurrence  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
        assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
        assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4


if __name__ == "__main__":
    unittest.main()
