import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import empty_dit  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert empty_dit([{},{},{}])==True
        assert empty_dit([{1,2},{},{}])==False
        assert empty_dit({})==True


if __name__ == "__main__":
    unittest.main()
