import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import surfacearea_cylinder  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert surfacearea_cylinder(10,5)==942.45
        assert surfacearea_cylinder(4,5)==226.18800000000002
        assert surfacearea_cylinder(4,10)==351.848


if __name__ == "__main__":
    unittest.main()
