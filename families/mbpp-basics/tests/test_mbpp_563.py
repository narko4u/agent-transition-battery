import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import extract_values  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
        assert extract_values('"python","program","language"')==['python','program','language']
        assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']


if __name__ == "__main__":
    unittest.main()
