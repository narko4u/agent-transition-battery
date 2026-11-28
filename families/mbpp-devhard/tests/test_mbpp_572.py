import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import two_unique_nums  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
        assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
        assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]


if __name__ == "__main__":
    unittest.main()
