import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Split  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Split([1,2,3,4,5,6]) == [1,3,5]
        assert Split([10,11,12,13]) == [11,13]
        assert Split([7,8,9,1]) == [7,9,1]


if __name__ == "__main__":
    unittest.main()
