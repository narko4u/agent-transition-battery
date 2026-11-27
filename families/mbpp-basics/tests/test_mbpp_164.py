import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import div_sum  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert are_equivalent(36, 57) == False
        assert are_equivalent(2, 4) == False
        assert are_equivalent(23, 47) == True


if __name__ == "__main__":
    unittest.main()
