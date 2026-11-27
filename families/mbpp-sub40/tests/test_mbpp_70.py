import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_equal_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
        assert get_equal([(1, 2, 3), (4, 5, 6, 7)]) == False
        assert get_equal([(1, 2), (3, 4)]) == True


if __name__ == "__main__":
    unittest.main()
