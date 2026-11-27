import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import kth_element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert kth_element([12,3,5,7,19], 2) == 3
        assert kth_element([17,24,8,23], 3) == 8
        assert kth_element([16,21,25,36,4], 4) == 36


if __name__ == "__main__":
    unittest.main()
