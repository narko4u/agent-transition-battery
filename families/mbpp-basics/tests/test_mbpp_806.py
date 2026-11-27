import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import max_run_uppercase  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert max_run_uppercase('GeMKSForGERksISBESt') == 5
        assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
        assert max_run_uppercase('GooGLEFluTTER') == 4


if __name__ == "__main__":
    unittest.main()
