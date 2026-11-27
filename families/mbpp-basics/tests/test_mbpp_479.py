import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import first_Digit  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert first_Digit(123) == 1
        assert first_Digit(456) == 4
        assert first_Digit(12) == 1


if __name__ == "__main__":
    unittest.main()
