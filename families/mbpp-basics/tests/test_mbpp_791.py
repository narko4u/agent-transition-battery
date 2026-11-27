import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_nested  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
        assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
        assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
        assert remove_nested((3, 7, 9, (6, 8), (5,12), 12)) == (3, 7, 9, 12)


if __name__ == "__main__":
    unittest.main()
