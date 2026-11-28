import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import set_middle_bits  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert toggle_middle_bits(9) == 15
        assert toggle_middle_bits(10) == 12
        assert toggle_middle_bits(11) == 13
        assert toggle_middle_bits(0b1000001) == 0b1111111
        assert toggle_middle_bits(0b1001101) == 0b1110011


if __name__ == "__main__":
    unittest.main()
