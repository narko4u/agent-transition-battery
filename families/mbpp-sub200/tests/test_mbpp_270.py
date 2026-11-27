import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_even_and_even_index  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
        assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
        assert sum_even_and_even_index([5, 6, 12, 1]) == 12


if __name__ == "__main__":
    unittest.main()
