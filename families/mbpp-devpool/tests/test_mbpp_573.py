import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import unique_product  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
        assert unique_product([1, 2, 3, 1,]) == 6
        assert unique_product([7, 8, 9, 0, 1, 1]) == 0


if __name__ == "__main__":
    unittest.main()
