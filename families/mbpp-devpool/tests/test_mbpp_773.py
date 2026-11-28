import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import occurance_substring  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert occurance_substring('python programming, python language','python')==('python', 0, 6)
        assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
        assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
        assert occurance_substring('c++ programming, c++ language','python')==None


if __name__ == "__main__":
    unittest.main()
