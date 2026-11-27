import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_solution  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert find_solution(2, 3, 7) == (2, 1)
        assert find_solution(4, 2, 7) == None
        assert find_solution(1, 13, 17) == (4, 1)


if __name__ == "__main__":
    unittest.main()
