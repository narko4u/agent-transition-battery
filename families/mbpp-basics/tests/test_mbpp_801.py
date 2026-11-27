import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import test_three_equal  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert test_three_equal(1,1,1) == 3
        assert test_three_equal(-1,-2,-3) == 0
        assert test_three_equal(1,2,2) == 2


if __name__ == "__main__":
    unittest.main()
