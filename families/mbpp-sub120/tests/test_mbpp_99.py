import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import decimal_to_binary  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert decimal_to_binary(8) == '1000'
        assert decimal_to_binary(18) == '10010'
        assert decimal_to_binary(7) == '111'


if __name__ == "__main__":
    unittest.main()
