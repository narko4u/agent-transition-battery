import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import reverse_Array_Upto_K  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
        assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]
        assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]


if __name__ == "__main__":
    unittest.main()
