import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import odd_length_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert odd_length_sum([1,2,4]) == 14
        assert odd_length_sum([1,2,1,2]) == 15
        assert odd_length_sum([1,7]) == 8


if __name__ == "__main__":
    unittest.main()
