import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_series  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_series(6) == 12
        assert sum_series(10) == 30
        assert sum_series(9) == 25


if __name__ == "__main__":
    unittest.main()
