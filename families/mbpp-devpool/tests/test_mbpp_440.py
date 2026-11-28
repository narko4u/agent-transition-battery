import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_adverb_position  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
        assert find_adverb_position("seriously!! there are many roses")==(0, 9, 'seriously')
        assert find_adverb_position("unfortunately!! sita is going to home")==(0, 13, 'unfortunately')


if __name__ == "__main__":
    unittest.main()
