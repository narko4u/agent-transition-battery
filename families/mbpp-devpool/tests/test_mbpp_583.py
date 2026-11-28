import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import catalan_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert catalan_number(10)==16796
        assert catalan_number(9)==4862
        assert catalan_number(7)==429


if __name__ == "__main__":
    unittest.main()
