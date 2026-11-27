import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_lists  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
        assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
        assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1


if __name__ == "__main__":
    unittest.main()
