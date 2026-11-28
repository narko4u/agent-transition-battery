import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_odd  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_odd([1,2,3]) == [2]
        assert remove_odd([2,4,6]) == [2,4,6]
        assert remove_odd([10,20,3]) == [10,20]


if __name__ == "__main__":
    unittest.main()
