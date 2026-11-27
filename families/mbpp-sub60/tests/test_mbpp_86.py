import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import centered_hexagonal_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert centered_hexagonal_number(10) == 271
        assert centered_hexagonal_number(2) == 7
        assert centered_hexagonal_number(9) == 217


if __name__ == "__main__":
    unittest.main()
