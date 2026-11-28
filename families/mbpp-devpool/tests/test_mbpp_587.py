import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import list_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
        assert list_tuple([2, 4, 5, 6, 2, 3, 4, 4, 7])==(2, 4, 5, 6, 2, 3, 4, 4, 7)
        assert list_tuple([58,44,56])==(58,44,56)


if __name__ == "__main__":
    unittest.main()
