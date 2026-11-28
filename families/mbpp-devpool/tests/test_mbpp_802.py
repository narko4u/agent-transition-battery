import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_rotation  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_rotation([3,2,1]) == 1
        assert count_rotation([4,5,1,2,3]) == 2
        assert count_rotation([7,8,9,1,2,3]) == 3
        assert count_rotation([1,2,3]) == 0
        assert count_rotation([1,3,2]) == 2


if __name__ == "__main__":
    unittest.main()
