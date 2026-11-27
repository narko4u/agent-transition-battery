import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import square_nums  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        assert square_nums([10,20,30])==([100,400,900])
        assert square_nums([12,15])==([144,225])


if __name__ == "__main__":
    unittest.main()
