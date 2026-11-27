import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sequential_search  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
        assert sequential_search([12, 32, 45, 62, 35, 47, 44, 61],61) == (True, 7)
        assert sequential_search([9, 10, 17, 19, 22, 39, 48, 56],48) == (True, 6)


if __name__ == "__main__":
    unittest.main()
