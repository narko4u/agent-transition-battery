import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import number_ctr  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert number_ctr('program2bedone') == 1
        assert number_ctr('3wonders') == 1
        assert number_ctr('123') == 3
        assert number_ctr('3wond-1ers2') == 3


if __name__ == "__main__":
    unittest.main()
