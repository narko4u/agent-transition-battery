import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_nonagonal  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_nonagonal(10) == 325
        assert is_nonagonal(15) == 750
        assert is_nonagonal(18) == 1089


if __name__ == "__main__":
    unittest.main()
