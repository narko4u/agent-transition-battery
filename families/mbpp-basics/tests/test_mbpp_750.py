import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import add_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
        assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
        assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]


if __name__ == "__main__":
    unittest.main()
