import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_element  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_element(["green", "orange", "black", "white"],'blue')==False
        assert check_element([1,2,3,4],7)==False
        assert check_element(["green", "green", "green", "green"],'green')==True


if __name__ == "__main__":
    unittest.main()
