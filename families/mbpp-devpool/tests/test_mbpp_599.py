import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import sum_average  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert sum_average(10)==(55, 5.5)
        assert sum_average(15)==(120, 8.0)
        assert sum_average(20)==(210, 10.5)


if __name__ == "__main__":
    unittest.main()
