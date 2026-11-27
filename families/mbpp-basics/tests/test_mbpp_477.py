import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_lower  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_lower("InValid") == "invalid"
        assert is_lower("TruE") == "true"
        assert is_lower("SenTenCE") == "sentence"


if __name__ == "__main__":
    unittest.main()
