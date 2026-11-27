import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import len_log  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert len_log(["python","PHP","bigdata"]) == 7
        assert len_log(["a","ab","abc"]) == 3
        assert len_log(["small","big","tall"]) == 5


if __name__ == "__main__":
    unittest.main()
