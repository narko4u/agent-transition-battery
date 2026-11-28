import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import Split  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert Split([1,2,3,4,5]) == [2,4]
        assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]
        assert Split ([8,12,15,19]) == [8,12]


if __name__ == "__main__":
    unittest.main()
