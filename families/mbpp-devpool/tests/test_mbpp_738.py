import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import geometric_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert geometric_sum(7) == 1.9921875
        assert geometric_sum(4) == 1.9375
        assert geometric_sum(8) == 1.99609375


if __name__ == "__main__":
    unittest.main()
