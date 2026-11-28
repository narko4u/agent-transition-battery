import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sequence  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sequence(10) == 6
        assert sequence(2) == 1
        assert sequence(3) == 2


if __name__ == "__main__":
    unittest.main()
