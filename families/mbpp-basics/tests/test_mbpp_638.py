import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import wind_chill  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert wind_chill(120,35)==40
        assert wind_chill(40,20)==19
        assert wind_chill(10,8)==6


if __name__ == "__main__":
    unittest.main()
