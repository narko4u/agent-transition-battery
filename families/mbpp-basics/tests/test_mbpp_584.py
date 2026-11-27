import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_adverbs  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
        assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
        assert find_adverbs("Complete the task quickly") == '18-25: quickly'


if __name__ == "__main__":
    unittest.main()
