import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_Occ  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_Occ("hello","l") == "heo"
        assert remove_Occ("abcda","a") == "bcd"
        assert remove_Occ("PHP","P") == "H"


if __name__ == "__main__":
    unittest.main()
