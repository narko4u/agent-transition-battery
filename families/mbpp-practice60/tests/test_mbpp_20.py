import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_woodall  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_woodall(383) == True
        assert is_woodall(254) == False
        assert is_woodall(200) == False


if __name__ == "__main__":
    unittest.main()
