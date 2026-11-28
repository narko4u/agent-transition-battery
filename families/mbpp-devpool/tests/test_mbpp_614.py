import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import cummulative_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
        assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
        assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44


if __name__ == "__main__":
    unittest.main()
