import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import test_duplicate  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert test_duplicate(([1,2,3,4,5]))==False
        assert test_duplicate(([1,2,3,4, 4]))==True
        assert test_duplicate([1,1,2,2,3,3,4,4,5])==True


if __name__ == "__main__":
    unittest.main()
