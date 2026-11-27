import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Parity  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Parity(12) == False
        assert find_Parity(7) == True
        assert find_Parity(10) == False


if __name__ == "__main__":
    unittest.main()
