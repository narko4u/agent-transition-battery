import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import smallest_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert smallest_num([10, 20, 1, 45, 99]) == 1
        assert smallest_num([1, 2, 3]) == 1
        assert smallest_num([45, 46, 50, 60]) == 45


if __name__ == "__main__":
    unittest.main()
