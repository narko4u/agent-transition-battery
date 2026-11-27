import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import parabola_directrix  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert parabola_directrix(5,3,2)==-198
        assert parabola_directrix(9,8,4)==-2336
        assert parabola_directrix(2,4,6)==-130


if __name__ == "__main__":
    unittest.main()
