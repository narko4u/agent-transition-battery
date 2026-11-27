import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import add_string  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
        assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']
        assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']


if __name__ == "__main__":
    unittest.main()
