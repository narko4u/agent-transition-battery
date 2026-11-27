import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import similar_elements  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
        assert set(similar_elements((1, 2, 3, 4),(5, 4, 3, 7))) == set((3, 4))
        assert set(similar_elements((11, 12, 14, 13),(17, 15, 14, 13))) == set((13, 14))


if __name__ == "__main__":
    unittest.main()
