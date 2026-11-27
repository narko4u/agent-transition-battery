import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import even_bit_set_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert even_bit_set_number(10) == 10
        assert even_bit_set_number(20) == 30
        assert even_bit_set_number(30) == 30


if __name__ == "__main__":
    unittest.main()
