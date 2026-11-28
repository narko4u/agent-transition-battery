import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import rearrange_bigger  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert rearrange_bigger(12)==21
        assert rearrange_bigger(10)==False
        assert rearrange_bigger(102)==120


if __name__ == "__main__":
    unittest.main()
