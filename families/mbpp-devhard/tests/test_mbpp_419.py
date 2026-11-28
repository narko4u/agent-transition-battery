import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import round_and_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
        assert round_and_sum([5,2,9,24.3,29])==345
        assert round_and_sum([25.0,56.7,89.2])==513


if __name__ == "__main__":
    unittest.main()
