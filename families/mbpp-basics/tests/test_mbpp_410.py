import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import min_val  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
        assert min_val(['Python', 15, 20, 25])==15
        assert min_val(['Python', 30, 20, 40, 50, 'version'])==20


if __name__ == "__main__":
    unittest.main()
