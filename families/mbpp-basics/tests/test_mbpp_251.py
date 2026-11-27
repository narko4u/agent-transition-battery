import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import insert_element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
        assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']
        assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']


if __name__ == "__main__":
    unittest.main()
