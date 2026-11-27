import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_lucas  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_lucas(9) == 76
        assert find_lucas(4) == 7
        assert find_lucas(3) == 4


if __name__ == "__main__":
    unittest.main()
