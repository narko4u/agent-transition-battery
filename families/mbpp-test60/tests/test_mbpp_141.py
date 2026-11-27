import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import pancake_sort  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
        assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
        assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]


if __name__ == "__main__":
    unittest.main()
