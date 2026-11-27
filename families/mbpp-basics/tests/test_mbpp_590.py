import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import polar_rect  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
        assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
        assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))


if __name__ == "__main__":
    unittest.main()
