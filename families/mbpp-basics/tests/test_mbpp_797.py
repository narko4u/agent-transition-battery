import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_odd  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_in_range(2,5) == 8
        assert sum_in_range(5,7) == 12
        assert sum_in_range(7,13) == 40


if __name__ == "__main__":
    unittest.main()
