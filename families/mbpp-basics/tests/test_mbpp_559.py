import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_sub_array_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
        assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
        assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10


if __name__ == "__main__":
    unittest.main()
