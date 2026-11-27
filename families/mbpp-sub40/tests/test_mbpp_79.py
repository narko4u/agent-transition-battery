import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import word_len  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert word_len("Hadoop") == False
        assert word_len("great") == True
        assert word_len("structure") == True


if __name__ == "__main__":
    unittest.main()
