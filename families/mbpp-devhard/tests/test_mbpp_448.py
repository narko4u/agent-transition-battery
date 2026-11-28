import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import cal_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert cal_sum(9) == 49
        assert cal_sum(10) == 66
        assert cal_sum(11) == 88


if __name__ == "__main__":
    unittest.main()
