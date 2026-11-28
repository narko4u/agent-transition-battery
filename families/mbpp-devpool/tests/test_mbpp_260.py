import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import newman_prime  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert newman_prime(3) == 7
        assert newman_prime(4) == 17
        assert newman_prime(5) == 41


if __name__ == "__main__":
    unittest.main()
