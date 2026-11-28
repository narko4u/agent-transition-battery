import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import tuple_str_int  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
        assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
        assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
        assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)


if __name__ == "__main__":
    unittest.main()
