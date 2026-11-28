import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import replace_spaces  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
        assert replace_spaces('The_Avengers') == 'The Avengers'
        assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'


if __name__ == "__main__":
    unittest.main()
