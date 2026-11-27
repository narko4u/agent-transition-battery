import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_octagonal  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_octagonal(5) == 65
        assert is_octagonal(10) == 280
        assert is_octagonal(15) == 645


if __name__ == "__main__":
    unittest.main()
