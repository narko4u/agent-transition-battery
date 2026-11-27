import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import bitwise_xor  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
        assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
        assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)


if __name__ == "__main__":
    unittest.main()
