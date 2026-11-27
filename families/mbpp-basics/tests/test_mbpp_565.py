import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import split  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert split('python') == ['p','y','t','h','o','n']
        assert split('Name') == ['N','a','m','e']
        assert split('program') == ['p','r','o','g','r','a','m']


if __name__ == "__main__":
    unittest.main()
