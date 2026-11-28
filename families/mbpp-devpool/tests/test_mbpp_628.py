import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import replace_spaces  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
        assert replace_spaces("I am a Programmer") == 'I%20am%20a%20Programmer'
        assert replace_spaces("I love Coding") == 'I%20love%20Coding'


if __name__ == "__main__":
    unittest.main()
