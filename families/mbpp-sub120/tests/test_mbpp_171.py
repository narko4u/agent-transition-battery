import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import perimeter_pentagon  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert perimeter_pentagon(5) == 25
        assert perimeter_pentagon(10) == 50
        assert perimeter_pentagon(15) == 75


if __name__ == "__main__":
    unittest.main()
