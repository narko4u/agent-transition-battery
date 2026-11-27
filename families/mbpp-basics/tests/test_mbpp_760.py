import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import unique_Element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert unique_Element([1,1,1]) == True
        assert unique_Element([1,2,1,2]) == False
        assert unique_Element([1,2,3,4,5]) == False


if __name__ == "__main__":
    unittest.main()
