import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import validate  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert validate(1234) == True
        assert validate(51241) == False
        assert validate(321) == True


if __name__ == "__main__":
    unittest.main()
