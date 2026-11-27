import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_integer  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_integer("python")==False
        assert check_integer("1")==True
        assert check_integer("12345")==True


if __name__ == "__main__":
    unittest.main()
