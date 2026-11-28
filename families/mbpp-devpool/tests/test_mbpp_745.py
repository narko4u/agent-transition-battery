import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import divisible_by_digits  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
        assert divisible_by_digits(20,25)==[22, 24]


if __name__ == "__main__":
    unittest.main()
