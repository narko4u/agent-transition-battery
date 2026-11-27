import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_element_in_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
        assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3
        assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1


if __name__ == "__main__":
    unittest.main()
