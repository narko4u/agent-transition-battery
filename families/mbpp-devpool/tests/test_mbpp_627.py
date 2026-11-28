import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_First_Missing  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_First_Missing([0,1,2,3]) == 4
        assert find_First_Missing([0,1,2,6,9]) == 3
        assert find_First_Missing([2,3,5,8,9]) == 0


if __name__ == "__main__":
    unittest.main()
