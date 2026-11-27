import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_integer  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_integer([1,2,'abc',1.2]) == 2
        assert count_integer([1,2,3]) == 3
        assert count_integer([1,1.2,4,5.1]) == 2


if __name__ == "__main__":
    unittest.main()
