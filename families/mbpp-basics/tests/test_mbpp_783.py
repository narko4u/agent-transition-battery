import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import rgb_to_hsv  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
        assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
        assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)


if __name__ == "__main__":
    unittest.main()
