import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import get_total_number_of_sequences  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert get_total_number_of_sequences(10, 4) == 4
        assert get_total_number_of_sequences(5, 2) == 6
        assert get_total_number_of_sequences(16, 3) == 84


if __name__ == "__main__":
    unittest.main()
