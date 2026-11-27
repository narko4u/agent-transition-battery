import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import last_Digit_Factorial  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert last_Digit_Factorial(4) == 4
        assert last_Digit_Factorial(21) == 0
        assert last_Digit_Factorial(30) == 0


if __name__ == "__main__":
    unittest.main()
