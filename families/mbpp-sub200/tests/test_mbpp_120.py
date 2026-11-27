import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_product_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
        assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
        assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484


if __name__ == "__main__":
    unittest.main()
