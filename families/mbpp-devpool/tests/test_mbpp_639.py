import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sample_nam  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
        assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
        assert sample_nam(["abcd", "Python", "abba", "aba"])==6


if __name__ == "__main__":
    unittest.main()
