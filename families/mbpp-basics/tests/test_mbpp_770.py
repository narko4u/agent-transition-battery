import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import odd_num_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert odd_num_sum(2) == 82
        assert odd_num_sum(3) == 707
        assert odd_num_sum(4) == 3108


if __name__ == "__main__":
    unittest.main()
