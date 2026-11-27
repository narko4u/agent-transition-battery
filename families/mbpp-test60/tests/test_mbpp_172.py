import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_occurance  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_occurance("letstdlenstdporstd") == 3
        assert count_occurance("truststdsolensporsd") == 1
        assert count_occurance("makestdsostdworthit") == 2
        assert count_occurance("stds") == 1
        assert count_occurance("") == 0


if __name__ == "__main__":
    unittest.main()
