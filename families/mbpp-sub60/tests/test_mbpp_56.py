import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import rev  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check(70) == False
        assert check(23) == False
        assert check(73) == True


if __name__ == "__main__":
    unittest.main()
