import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import left_insertion  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert left_insertion([1,2,4,5],6)==4
        assert left_insertion([1,2,4,5],3)==2
        assert left_insertion([1,2,4,5],7)==4


if __name__ == "__main__":
    unittest.main()
