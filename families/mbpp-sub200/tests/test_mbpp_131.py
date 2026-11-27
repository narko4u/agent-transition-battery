import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import reverse_vowels  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert reverse_vowels("Python") == "Python"
        assert reverse_vowels("USA") == "ASU"
        assert reverse_vowels("ab") == "ab"


if __name__ == "__main__":
    unittest.main()
