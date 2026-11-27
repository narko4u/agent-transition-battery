import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_samepatterns  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
        assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
        assert is_samepatterns(["red","green","greenn"], ["a","b"])==False


if __name__ == "__main__":
    unittest.main()
