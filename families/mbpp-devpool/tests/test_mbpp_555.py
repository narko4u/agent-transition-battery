import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import difference  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert difference(3) == 30
        assert difference(5) == 210
        assert difference(2) == 6


if __name__ == "__main__":
    unittest.main()
