import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import _sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert _sum([1, 2, 3]) == 6
        assert _sum([15, 12, 13, 10]) == 50
        assert _sum([0, 1, 2]) == 3


if __name__ == "__main__":
    unittest.main()
