import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_product  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_product([3, 100, 4, 5, 150, 6]) == 3000
        assert max_product([4, 42, 55, 68, 80]) == 50265600
        assert max_product([10, 22, 9, 33, 21, 50, 41, 60]) == 2460


if __name__ == "__main__":
    unittest.main()
