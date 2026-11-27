import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import power_base_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert power_base_sum(2,100)==115
        assert power_base_sum(8,10)==37
        assert power_base_sum(8,15)==62
        assert power_base_sum(3,3)==9


if __name__ == "__main__":
    unittest.main()
