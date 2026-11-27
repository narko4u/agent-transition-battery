import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import odd_values_string  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert odd_values_string('abcdef') == 'ace'
        assert odd_values_string('python') == 'pto'
        assert odd_values_string('data') == 'dt'
        assert odd_values_string('lambs') == 'lms'


if __name__ == "__main__":
    unittest.main()
