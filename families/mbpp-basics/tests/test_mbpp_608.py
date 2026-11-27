import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import bell_Number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert bell_Number(2) == 2
        assert bell_Number(3) == 5
        assert bell_Number(4) == 15


if __name__ == "__main__":
    unittest.main()
