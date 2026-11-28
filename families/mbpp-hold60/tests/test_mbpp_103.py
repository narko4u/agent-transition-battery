import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import eulerian_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert eulerian_num(3, 1) == 4
        assert eulerian_num(4, 1) == 11
        assert eulerian_num(5, 3) == 26


if __name__ == "__main__":
    unittest.main()
