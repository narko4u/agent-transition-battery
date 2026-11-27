import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import positive_count  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
        assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69
        assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56


if __name__ == "__main__":
    unittest.main()
