import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_Average_Of_Cube  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_Average_Of_Cube(2) == 4.5
        assert find_Average_Of_Cube(3) == 12
        assert find_Average_Of_Cube(1) == 1


if __name__ == "__main__":
    unittest.main()
