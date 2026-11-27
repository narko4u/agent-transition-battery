import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import count_reverse_pairs  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
        assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1
        assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2


if __name__ == "__main__":
    unittest.main()
