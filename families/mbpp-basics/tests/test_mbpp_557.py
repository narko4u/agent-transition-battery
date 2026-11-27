import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import toggle_string  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert toggle_string("Python")==("pYTHON")
        assert toggle_string("Pangram")==("pANGRAM")
        assert toggle_string("LIttLE")==("liTTle")


if __name__ == "__main__":
    unittest.main()
