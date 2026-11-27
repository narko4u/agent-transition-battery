import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_max_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_max_sum(60) == 106
        assert get_max_sum(10) == 12
        assert get_max_sum(2) == 2


if __name__ == "__main__":
    unittest.main()
