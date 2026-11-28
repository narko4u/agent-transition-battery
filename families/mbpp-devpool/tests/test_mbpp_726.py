import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import multiply_elements  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
        assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
        assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
        assert multiply_elements((12,)) == ()


if __name__ == "__main__":
    unittest.main()
