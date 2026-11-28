import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_Occurrence  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
        assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
        assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2


if __name__ == "__main__":
    unittest.main()
