import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import maximum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert maximum(5,10) == 10
        assert maximum(-1,-2) == -1
        assert maximum(9,7) == 9


if __name__ == "__main__":
    unittest.main()
