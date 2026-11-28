import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_expression  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_expression("{()}[{}]") == True
        assert check_expression("{()}[{]") == False
        assert check_expression("{()}[{}][]({})") == True


if __name__ == "__main__":
    unittest.main()
