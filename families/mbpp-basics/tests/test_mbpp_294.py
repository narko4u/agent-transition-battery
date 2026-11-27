import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_val  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
        assert max_val(['Python', 15, 20, 25])==25
        assert max_val(['Python', 30, 20, 40, 50, 'version'])==50


if __name__ == "__main__":
    unittest.main()
