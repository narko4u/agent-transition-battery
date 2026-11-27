import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import amicable_numbers_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert amicable_numbers_sum(999)==504
        assert amicable_numbers_sum(9999)==31626
        assert amicable_numbers_sum(99)==0


if __name__ == "__main__":
    unittest.main()
