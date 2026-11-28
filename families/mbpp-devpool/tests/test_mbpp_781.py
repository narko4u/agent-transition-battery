import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_divisors  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_divisors(10)
        assert not count_divisors(100)
        assert count_divisors(125)


if __name__ == "__main__":
    unittest.main()
