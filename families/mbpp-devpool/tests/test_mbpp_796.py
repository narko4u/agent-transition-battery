import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import return_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
        assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
        assert return_sum({'a': 36, 'b':39, 'c':49}) == 124


if __name__ == "__main__":
    unittest.main()
