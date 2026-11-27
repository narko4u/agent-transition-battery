import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import dif_Square  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert dif_Square(5) == True
        assert dif_Square(10) == False
        assert dif_Square(15) == True


if __name__ == "__main__":
    unittest.main()
