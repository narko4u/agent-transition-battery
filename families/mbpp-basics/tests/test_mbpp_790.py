import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import even_position  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert even_position([3,2,1]) == False
        assert even_position([1,2,3]) == False
        assert even_position([2,1,4]) == True


if __name__ == "__main__":
    unittest.main()
