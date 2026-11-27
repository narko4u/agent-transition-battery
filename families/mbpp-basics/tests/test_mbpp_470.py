import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import add_pairwise  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
        assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
        assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)


if __name__ == "__main__":
    unittest.main()
