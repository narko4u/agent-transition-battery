import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import search  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert search([1,1,2,2,3]) == 3
        assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8
        assert search([1,2,2,3,3,4,4]) == 1


if __name__ == "__main__":
    unittest.main()
