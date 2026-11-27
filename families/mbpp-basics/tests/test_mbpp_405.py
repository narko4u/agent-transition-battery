import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_tuplex  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
        assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
        assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True


if __name__ == "__main__":
    unittest.main()
