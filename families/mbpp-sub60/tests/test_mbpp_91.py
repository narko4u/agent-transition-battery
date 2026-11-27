import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_substring  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
        assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
        assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True


if __name__ == "__main__":
    unittest.main()
