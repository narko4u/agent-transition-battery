import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum(10,15) == 6
        assert sum(100,150) == 93
        assert sum(4,6) == 3


if __name__ == "__main__":
    unittest.main()
