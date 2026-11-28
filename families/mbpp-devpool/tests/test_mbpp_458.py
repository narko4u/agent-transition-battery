import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import rectangle_area  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert rectangle_area(10,20)==200
        assert rectangle_area(10,5)==50
        assert rectangle_area(4,2)==8


if __name__ == "__main__":
    unittest.main()
