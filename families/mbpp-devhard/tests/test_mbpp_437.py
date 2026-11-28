import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_odd  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_odd("python")==("yhn")
        assert remove_odd("program")==("rga")
        assert remove_odd("language")==("agae")


if __name__ == "__main__":
    unittest.main()
