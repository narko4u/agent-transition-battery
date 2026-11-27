import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_div  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_div(8)==7
        assert sum_div(12)==16
        assert sum_div(7)==1


if __name__ == "__main__":
    unittest.main()
