import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_median  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
        assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
        assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0


if __name__ == "__main__":
    unittest.main()
