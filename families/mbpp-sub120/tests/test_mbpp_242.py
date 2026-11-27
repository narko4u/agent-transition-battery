import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_charac  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_charac("python programming")==18
        assert count_charac("language")==8
        assert count_charac("words")==5


if __name__ == "__main__":
    unittest.main()
