import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_ludic  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_ludic(10) == [1, 2, 3, 5, 7]
        assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
        assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]


if __name__ == "__main__":
    unittest.main()
