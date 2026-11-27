import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_not_prime  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_not_prime(2) == False
        assert is_not_prime(10) == True
        assert is_not_prime(35) == True
        assert is_not_prime(37) == False


if __name__ == "__main__":
    unittest.main()
