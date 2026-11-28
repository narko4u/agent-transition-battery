import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_subarray_product  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
        assert max_subarray_product([6, -3, -10, 0, 2]) == 180
        assert max_subarray_product([-2, -40, 0, -2, -3]) == 80


if __name__ == "__main__":
    unittest.main()
