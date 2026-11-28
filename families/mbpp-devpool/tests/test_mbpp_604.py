import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import reverse_words  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert reverse_words("python program")==("program python")
        assert reverse_words("java language")==("language java")
        assert reverse_words("indian man")==("man indian")


if __name__ == "__main__":
    unittest.main()
