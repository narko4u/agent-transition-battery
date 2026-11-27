import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import tetrahedral_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert tetrahedral_number(5) == 35
        assert tetrahedral_number(6) == 56
        assert tetrahedral_number(7) == 84


if __name__ == "__main__":
    unittest.main()
