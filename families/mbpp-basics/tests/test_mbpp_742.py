import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import area_tetrahedron  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert area_tetrahedron(3)==15.588457268119894
        assert area_tetrahedron(20)==692.8203230275509
        assert area_tetrahedron(10)==173.20508075688772


if __name__ == "__main__":
    unittest.main()
