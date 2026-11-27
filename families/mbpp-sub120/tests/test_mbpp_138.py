import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_Sum_Of_Powers_Of_Two  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_Sum_Of_Powers_Of_Two(10) == True
        assert is_Sum_Of_Powers_Of_Two(7) == False
        assert is_Sum_Of_Powers_Of_Two(14) == True


if __name__ == "__main__":
    unittest.main()
