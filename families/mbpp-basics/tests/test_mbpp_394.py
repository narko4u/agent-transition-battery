import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_distinct  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_distinct((1, 4, 5, 6, 1, 4)) == False
        assert check_distinct((1, 4, 5, 6)) == True
        assert check_distinct((2, 3, 4, 5, 6)) == True


if __name__ == "__main__":
    unittest.main()
