import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import snake_to_camel  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert snake_to_camel('python_program')=='PythonProgram'
        assert snake_to_camel('python_language')==('PythonLanguage')
        assert snake_to_camel('programming_language')==('ProgrammingLanguage')


if __name__ == "__main__":
    unittest.main()
