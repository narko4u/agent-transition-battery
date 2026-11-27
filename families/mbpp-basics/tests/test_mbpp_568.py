import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import empty_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert empty_list(5)==[{},{},{},{},{}]
        assert empty_list(6)==[{},{},{},{},{},{}]
        assert empty_list(7)==[{},{},{},{},{},{},{}]


if __name__ == "__main__":
    unittest.main()
