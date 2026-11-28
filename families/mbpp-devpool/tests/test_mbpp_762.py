import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_monthnumber_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_monthnumber_number(6)==True
        assert check_monthnumber_number(2)==False
        assert check_monthnumber_number(12)==False


if __name__ == "__main__":
    unittest.main()
