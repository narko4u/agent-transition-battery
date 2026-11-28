import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import extract_freq  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
        assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
        assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4


if __name__ == "__main__":
    unittest.main()
