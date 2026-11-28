import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_of_digits  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_of_digits([10,2,56])==14
        assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
        assert sum_of_digits([10,20,-4,5,-70])==19


if __name__ == "__main__":
    unittest.main()
