import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_even_pair  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_even_pair([5, 4, 7, 2, 1]) == 4
        assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
        assert find_even_pair([1, 2, 3]) == 1


if __name__ == "__main__":
    unittest.main()
