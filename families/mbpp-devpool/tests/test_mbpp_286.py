import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_sub_array_sum_repeated  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
        assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
        assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1


if __name__ == "__main__":
    unittest.main()
