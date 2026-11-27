import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import unique_sublists  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
        assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
        assert unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}


if __name__ == "__main__":
    unittest.main()
