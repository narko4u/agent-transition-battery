import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import comb_sort  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
        assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
        assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]


if __name__ == "__main__":
    unittest.main()
