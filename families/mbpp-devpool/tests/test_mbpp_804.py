import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_product_even  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_product_even([1,2,3])
        assert is_product_even([1,2,1,4])
        assert not is_product_even([1,1])


if __name__ == "__main__":
    unittest.main()
