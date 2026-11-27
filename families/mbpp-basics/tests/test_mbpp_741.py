import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import all_Characters_Same  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert all_Characters_Same("python") == False
        assert all_Characters_Same("aaa") == True
        assert all_Characters_Same("data") == False


if __name__ == "__main__":
    unittest.main()
