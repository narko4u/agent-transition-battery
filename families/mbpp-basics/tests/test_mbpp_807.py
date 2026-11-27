import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import first_odd  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert first_odd([1,3,5]) == 1
        assert first_odd([2,4,1,3]) == 1
        assert first_odd ([8,9,1]) == 9


if __name__ == "__main__":
    unittest.main()
