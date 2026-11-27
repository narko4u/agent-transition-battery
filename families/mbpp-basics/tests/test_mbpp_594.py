import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import diff_even_odd  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert diff_even_odd([1,3,5,7,4,1,6,8])==3
        assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
        assert diff_even_odd([1,5,7,9,10])==9


if __name__ == "__main__":
    unittest.main()
