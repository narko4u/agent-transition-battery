import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_Of_Subarray_Prod  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_Of_Subarray_Prod([1,2,3]) == 20
        assert sum_Of_Subarray_Prod([1,2]) == 5
        assert sum_Of_Subarray_Prod([1,2,3,4]) == 84


if __name__ == "__main__":
    unittest.main()
