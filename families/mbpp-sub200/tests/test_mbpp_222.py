import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import check_type  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert check_type((5, 6, 7, 3, 5, 6) ) == True
        assert check_type((1, 2, "4") ) == False
        assert check_type((3, 2, 1, 4, 5) ) == True


if __name__ == "__main__":
    unittest.main()
