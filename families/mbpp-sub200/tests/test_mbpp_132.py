import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import tup_string  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
        assert tup_string(('p','y','t','h','o','n'))==("python")
        assert tup_string(('p','r','o','g','r','a','m'))==("program")


if __name__ == "__main__":
    unittest.main()
