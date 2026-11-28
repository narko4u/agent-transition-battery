import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_length  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
        assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
        assert max_length([[5], [15,20,25]])==(3, [15,20,25])


if __name__ == "__main__":
    unittest.main()
