import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Even  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_Even(1) == False
        assert is_Even(2) == True
        assert is_Even(3) == False


if __name__ == "__main__":
    unittest.main()
