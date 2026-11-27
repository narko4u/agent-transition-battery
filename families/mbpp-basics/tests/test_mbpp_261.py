import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import division_elements  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
        assert division_elements((12, 6, 8, 16),(6, 3, 4, 4)) == (2, 2, 2, 4)
        assert division_elements((20, 14, 36, 18),(5, 7, 6, 9)) == (4, 2, 6, 2)


if __name__ == "__main__":
    unittest.main()
