import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_sublist  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_sublist([2,4,3,5,7],[3,7])==False
        assert is_sublist([2,4,3,5,7],[4,3])==True
        assert is_sublist([2,4,3,5,7],[1,6])==False


if __name__ == "__main__":
    unittest.main()
