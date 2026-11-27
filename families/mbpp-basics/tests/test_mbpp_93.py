import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import power  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert power(3,4) == 81
        assert power(2,3) == 8
        assert power(5,5) == 3125


if __name__ == "__main__":
    unittest.main()
