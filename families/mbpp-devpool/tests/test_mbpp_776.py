import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_vowels  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_vowels('bestinstareels') == 7
        assert count_vowels('partofthejourneyistheend') == 12
        assert count_vowels('amazonprime') == 5


if __name__ == "__main__":
    unittest.main()
