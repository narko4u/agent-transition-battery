import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_decimal  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_decimal('123.11')==True
        assert is_decimal('e666.86')==False
        assert is_decimal('3.124587')==False
        assert is_decimal('1.11')==True
        assert is_decimal('1.1.11')==False


if __name__ == "__main__":
    unittest.main()
