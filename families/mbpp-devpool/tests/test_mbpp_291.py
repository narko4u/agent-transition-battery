import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_no_of_ways  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_no_of_ways(2, 4) == 16
        assert count_no_of_ways(3, 2) == 6
        assert count_no_of_ways(4, 4) == 228


if __name__ == "__main__":
    unittest.main()
