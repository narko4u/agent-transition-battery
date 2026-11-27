import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Rotations  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Rotations("aaaa") == 1
        assert find_Rotations("ab") == 2
        assert find_Rotations("abc") == 3


if __name__ == "__main__":
    unittest.main()
