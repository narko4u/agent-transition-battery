import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_Primes_nums  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_Primes_nums(5) == 2
        assert count_Primes_nums(10) == 4
        assert count_Primes_nums(100) == 25


if __name__ == "__main__":
    unittest.main()
