import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import noprofit_noloss  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert noprofit_noloss(1500,1200)==False
        assert noprofit_noloss(100,100)==True
        assert noprofit_noloss(2000,5000)==False


if __name__ == "__main__":
    unittest.main()
