import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_negativenum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
        assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52
        assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894


if __name__ == "__main__":
    unittest.main()
