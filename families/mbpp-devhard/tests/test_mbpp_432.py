import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import median_trapezium  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert median_trapezium(15,25,35)==20
        assert median_trapezium(10,20,30)==15
        assert median_trapezium(6,9,4)==7.5


if __name__ == "__main__":
    unittest.main()
