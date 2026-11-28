import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import binomial_Coeff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_Of_product(3) == 15
        assert sum_Of_product(4) == 56
        assert sum_Of_product(1) == 1


if __name__ == "__main__":
    unittest.main()
