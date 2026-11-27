import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import extract_rear  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
        assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
        assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']


if __name__ == "__main__":
    unittest.main()
