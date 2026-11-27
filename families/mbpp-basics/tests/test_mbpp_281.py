import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import all_unique  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert all_unique([1,2,3]) == True
        assert all_unique([1,2,1,2]) == False
        assert all_unique([1,2,3,4,5]) == True


if __name__ == "__main__":
    unittest.main()
