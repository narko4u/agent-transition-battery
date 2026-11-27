import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
        assert max_sum([80, 60, 30, 40, 20, 10]) == 210
        assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138


if __name__ == "__main__":
    unittest.main()
