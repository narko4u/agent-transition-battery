import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import tuple_to_int  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert tuple_to_int((1,2,3))==123
        assert tuple_to_int((4,5,6))==456
        assert tuple_to_int((5,6,7))==567


if __name__ == "__main__":
    unittest.main()
