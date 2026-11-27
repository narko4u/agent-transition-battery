import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_difference  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
        assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
        assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23


if __name__ == "__main__":
    unittest.main()
