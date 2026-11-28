import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import left_rotate  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert left_rotate(16,2) == 64
        assert left_rotate(10,2) == 40
        assert left_rotate(99,3) == 792
        assert left_rotate(99,3) == 792
        assert left_rotate(0b0001,3) == 0b1000
        assert left_rotate(0b0101,3) == 0b101000
        assert left_rotate(0b11101,3) == 0b11101000


if __name__ == "__main__":
    unittest.main()
