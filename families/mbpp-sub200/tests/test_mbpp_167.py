import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import next_power_of_2  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert next_power_of_2(0) == 1
        assert next_power_of_2(5) == 8
        assert next_power_of_2(17) == 32


if __name__ == "__main__":
    unittest.main()
