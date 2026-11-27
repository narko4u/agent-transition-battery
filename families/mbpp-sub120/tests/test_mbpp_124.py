import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import angle_complex  # noqa: F401
import math


class TestCase(unittest.TestCase):
    def test_cases(self):
        assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
        assert math.isclose(angle_complex(2,1j), 0.4636476090008061, rel_tol=0.001)
        assert math.isclose(angle_complex(0,2j), 1.5707963267948966, rel_tol=0.001)


if __name__ == "__main__":
    unittest.main()
