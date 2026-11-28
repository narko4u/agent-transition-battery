import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import armstrong_number  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert armstrong_number(153)==True
        assert armstrong_number(259)==False
        assert armstrong_number(4458)==False


if __name__ == "__main__":
    unittest.main()
