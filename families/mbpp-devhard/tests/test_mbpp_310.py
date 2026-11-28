import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import string_to_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
        assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
        assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')


if __name__ == "__main__":
    unittest.main()
