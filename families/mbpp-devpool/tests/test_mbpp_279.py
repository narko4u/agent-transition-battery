import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_num_decagonal  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_num_decagonal(3) == 27
        assert is_num_decagonal(7) == 175
        assert is_num_decagonal(10) == 370


if __name__ == "__main__":
    unittest.main()
