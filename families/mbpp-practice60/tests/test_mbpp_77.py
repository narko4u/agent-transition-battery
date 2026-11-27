import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Diff  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_Diff (12345) == False
        assert is_Diff(1212112) == True
        assert is_Diff(1212) == False


if __name__ == "__main__":
    unittest.main()
