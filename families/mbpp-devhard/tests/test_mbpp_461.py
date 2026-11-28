import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import upper_ctr  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert upper_ctr('PYthon') == 1
        assert upper_ctr('BigData') == 1
        assert upper_ctr('program') == 0


if __name__ == "__main__":
    unittest.main()
