import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import convert  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert convert(1) == (1.0, 0.0)
        assert convert(4) == (4.0,0.0)
        assert convert(5) == (5.0,0.0)


if __name__ == "__main__":
    unittest.main()
