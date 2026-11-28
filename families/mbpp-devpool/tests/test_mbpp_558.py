import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import digit_distance_nums  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert digit_distance_nums(1,2) == 1
        assert digit_distance_nums(23,56) == 6
        assert digit_distance_nums(123,256) == 7


if __name__ == "__main__":
    unittest.main()
