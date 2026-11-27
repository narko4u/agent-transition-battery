import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import multiply_int  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert multiply_int(10,20)==200
        assert multiply_int(5,10)==50
        assert multiply_int(4,8)==32


if __name__ == "__main__":
    unittest.main()
