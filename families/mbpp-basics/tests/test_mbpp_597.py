import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_kth  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
        assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
        assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8


if __name__ == "__main__":
    unittest.main()
