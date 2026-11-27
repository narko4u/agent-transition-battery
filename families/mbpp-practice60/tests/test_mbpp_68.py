import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Monotonic  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_Monotonic([6, 5, 4, 4]) == True
        assert is_Monotonic([1, 2, 2, 3]) == True
        assert is_Monotonic([1, 3, 2]) == False


if __name__ == "__main__":
    unittest.main()
