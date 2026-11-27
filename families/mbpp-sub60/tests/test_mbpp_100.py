import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import next_smallest_palindrome  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert next_smallest_palindrome(99)==101
        assert next_smallest_palindrome(1221)==1331
        assert next_smallest_palindrome(120)==121


if __name__ == "__main__":
    unittest.main()
