import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_occurences  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
        assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
        assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}


if __name__ == "__main__":
    unittest.main()
