import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import dog_age  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert dog_age(12)==61
        assert dog_age(15)==73
        assert dog_age(24)==109


if __name__ == "__main__":
    unittest.main()
