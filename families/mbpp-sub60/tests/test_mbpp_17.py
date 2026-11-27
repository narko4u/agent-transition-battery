import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import square_perimeter  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert square_perimeter(10)==40
        assert square_perimeter(5)==20
        assert square_perimeter(4)==16


if __name__ == "__main__":
    unittest.main()
