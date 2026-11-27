import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import even_binomial_Coeff_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert even_binomial_Coeff_Sum(4) == 8
        assert even_binomial_Coeff_Sum(6) == 32
        assert even_binomial_Coeff_Sum(2) == 2


if __name__ == "__main__":
    unittest.main()
