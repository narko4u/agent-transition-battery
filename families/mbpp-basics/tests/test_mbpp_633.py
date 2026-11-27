import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import pair_xor_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert pair_xor_Sum([5,9,7,6],4) == 47
        assert pair_xor_Sum([7,3,5],3) == 12
        assert pair_xor_Sum([7,3],2) == 4


if __name__ == "__main__":
    unittest.main()
