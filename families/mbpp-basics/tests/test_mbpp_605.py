import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import prime_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert prime_num(13)==True
        assert prime_num(7)==True
        assert prime_num(-1010)==False


if __name__ == "__main__":
    unittest.main()
