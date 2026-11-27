import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_all_spaces  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_all_spaces('python  program')==('pythonprogram')
        assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
        assert remove_all_spaces('python                     program')==('pythonprogram')
        assert remove_all_spaces('   python                     program')=='pythonprogram'


if __name__ == "__main__":
    unittest.main()
