import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import substract_elements  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
        assert substract_elements((11, 2, 3), (24, 45 ,16)) == (-13, -43, -13)
        assert substract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)


if __name__ == "__main__":
    unittest.main()
