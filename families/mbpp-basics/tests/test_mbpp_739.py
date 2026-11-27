import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Index  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Index(2) == 4
        assert find_Index(3) == 14
        assert find_Index(4) == 45


if __name__ == "__main__":
    unittest.main()
