import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import loss_amount  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert loss_amount(1500,1200)==0
        assert loss_amount(100,200)==100
        assert loss_amount(2000,5000)==3000


if __name__ == "__main__":
    unittest.main()
