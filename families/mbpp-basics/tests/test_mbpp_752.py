import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import jacobsthal_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert jacobsthal_num(5) == 11
        assert jacobsthal_num(2) == 1
        assert jacobsthal_num(4) == 5
        assert jacobsthal_num(13) == 2731


if __name__ == "__main__":
    unittest.main()
