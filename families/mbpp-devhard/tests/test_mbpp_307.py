import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import colon_tuplex  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
        assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
        assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)


if __name__ == "__main__":
    unittest.main()
