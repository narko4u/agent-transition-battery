import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import minimum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert minimum(1,2) == 1
        assert minimum(-5,-4) == -5
        assert minimum(0,0) == 0


if __name__ == "__main__":
    unittest.main()
