import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import volume_cube  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert volume_cube(3)==27
        assert volume_cube(2)==8
        assert volume_cube(5)==125


if __name__ == "__main__":
    unittest.main()
