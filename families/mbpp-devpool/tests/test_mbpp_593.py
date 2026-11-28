import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import removezero_ip  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert removezero_ip("216.08.094.196")==('216.8.94.196')
        assert removezero_ip("12.01.024")==('12.1.24')
        assert removezero_ip("216.08.094.0196")==('216.8.94.196')


if __name__ == "__main__":
    unittest.main()
