import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_Pairs  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_Pairs([1,2,1],3) == 2
        assert count_Pairs([1,1,1,1],4) == 0
        assert count_Pairs([1,2,3,4,5],5) == 10


if __name__ == "__main__":
    unittest.main()
