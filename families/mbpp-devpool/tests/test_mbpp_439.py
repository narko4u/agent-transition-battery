import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import multiple_to_single  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert multiple_to_single([11, 33, 50])==113350
        assert multiple_to_single([-1,2,3,4,5,6])==-123456
        assert multiple_to_single([10,15,20,25])==10152025


if __name__ == "__main__":
    unittest.main()
