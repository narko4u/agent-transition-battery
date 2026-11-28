import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
        assert count_list([[1,2],[2,3],[4,5]]) == 3
        assert count_list([[1,0],[2,0]]) == 2


if __name__ == "__main__":
    unittest.main()
