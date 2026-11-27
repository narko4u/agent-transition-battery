import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import replace_blank  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert replace_blank("hello people",'@')==("hello@people")
        assert replace_blank("python program language",'$')==("python$program$language")
        assert replace_blank("blank space","-")==("blank-space")


if __name__ == "__main__":
    unittest.main()
