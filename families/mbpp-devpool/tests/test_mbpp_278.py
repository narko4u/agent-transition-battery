import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_first_elements  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
        assert count_first_elements((2, 9, (5, 7), 11) ) == 2
        assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4


if __name__ == "__main__":
    unittest.main()
