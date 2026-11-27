import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import lcs_of_three  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
        assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
        assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3


if __name__ == "__main__":
    unittest.main()
