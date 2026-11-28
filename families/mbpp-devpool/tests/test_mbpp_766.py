import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import pair_wise  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
        assert pair_wise([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]
        assert pair_wise([5,1,9,7,10])==[(5, 1), (1, 9), (9, 7), (7, 10)]
        assert pair_wise([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]


if __name__ == "__main__":
    unittest.main()
