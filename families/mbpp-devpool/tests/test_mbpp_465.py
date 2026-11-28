import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import drop_empty  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
        assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
        assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}


if __name__ == "__main__":
    unittest.main()
