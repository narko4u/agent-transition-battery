import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import extract_string  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
        assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
        assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']


if __name__ == "__main__":
    unittest.main()
