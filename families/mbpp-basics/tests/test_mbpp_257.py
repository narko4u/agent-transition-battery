import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import swap_numbers  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert swap_numbers(10,20)==(20,10)
        assert swap_numbers(15,17)==(17,15)
        assert swap_numbers(100,200)==(200,100)


if __name__ == "__main__":
    unittest.main()
