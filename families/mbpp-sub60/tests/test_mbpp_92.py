import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_undulating  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_undulating(1212121) == True
        assert is_undulating(1991) == False
        assert is_undulating(121) == True


if __name__ == "__main__":
    unittest.main()
