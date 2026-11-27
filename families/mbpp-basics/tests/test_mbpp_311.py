import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import set_left_most_unset_bit  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert set_left_most_unset_bit(10) == 14
        assert set_left_most_unset_bit(12) == 14
        assert set_left_most_unset_bit(15) == 15


if __name__ == "__main__":
    unittest.main()
