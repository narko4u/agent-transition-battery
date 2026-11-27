import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import long_words  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert long_words(3,"python is a programming language")==['python','programming','language']
        assert long_words(2,"writing a program")==['writing','program']
        assert long_words(5,"sorting list")==['sorting']


if __name__ == "__main__":
    unittest.main()
