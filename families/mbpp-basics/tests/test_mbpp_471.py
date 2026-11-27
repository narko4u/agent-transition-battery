import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_remainder  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
        assert find_remainder([1,1,1],1) == 0
        assert find_remainder([1,2,1],2) == 0


if __name__ == "__main__":
    unittest.main()
