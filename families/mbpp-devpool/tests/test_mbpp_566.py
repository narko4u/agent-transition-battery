import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_digits  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_digits(345)==12
        assert sum_digits(12)==3
        assert sum_digits(97)==16


if __name__ == "__main__":
    unittest.main()
