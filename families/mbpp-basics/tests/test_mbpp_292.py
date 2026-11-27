import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find(10,3) == 3
        assert find(4,2) == 2
        assert find(20,5) == 4


if __name__ == "__main__":
    unittest.main()
