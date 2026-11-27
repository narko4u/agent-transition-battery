import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import even_Power_Sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert even_Power_Sum(2) == 1056
        assert even_Power_Sum(3) == 8832
        assert even_Power_Sum(1) == 32


if __name__ == "__main__":
    unittest.main()
