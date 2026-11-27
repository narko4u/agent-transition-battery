import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import capital_words_spaces  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert capital_words_spaces("Python") == 'Python'
        assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
        assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'


if __name__ == "__main__":
    unittest.main()
