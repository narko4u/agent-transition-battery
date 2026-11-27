import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import string_to_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert string_to_list("python programming")==['python','programming']
        assert string_to_list("lists tuples strings")==['lists','tuples','strings']
        assert string_to_list("write a program")==['write','a','program']


if __name__ == "__main__":
    unittest.main()
