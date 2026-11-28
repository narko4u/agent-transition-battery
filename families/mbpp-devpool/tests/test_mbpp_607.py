import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_literals  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
        assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
        assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)


if __name__ == "__main__":
    unittest.main()
