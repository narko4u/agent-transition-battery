import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import second_smallest  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert second_smallest([1, 2, -8, -2, 0, -2])==-2
        assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5
        assert second_smallest([2,2])==None
        assert second_smallest([2,2,2])==None


if __name__ == "__main__":
    unittest.main()
