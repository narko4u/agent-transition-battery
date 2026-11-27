import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import median_numbers  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert median_numbers(25,55,65)==55.0
        assert median_numbers(20,10,30)==20.0
        assert median_numbers(15,45,75)==45.0


if __name__ == "__main__":
    unittest.main()
