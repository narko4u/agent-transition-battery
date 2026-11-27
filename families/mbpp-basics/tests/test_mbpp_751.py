import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_min_heap_helper  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
        assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
        assert check_min_heap([2, 10, 4, 5, 3, 15]) == False


if __name__ == "__main__":
    unittest.main()
