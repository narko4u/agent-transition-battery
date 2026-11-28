import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_lowercase  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_lowercase("PYTHon")==('PYTH')
        assert remove_lowercase("FInD")==('FID')
        assert remove_lowercase("STRinG")==('STRG')


if __name__ == "__main__":
    unittest.main()
