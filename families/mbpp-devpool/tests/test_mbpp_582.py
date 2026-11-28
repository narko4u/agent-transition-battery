import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import my_dict  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert my_dict({10})==False
        assert my_dict({11})==False
        assert my_dict({})==True


if __name__ == "__main__":
    unittest.main()
