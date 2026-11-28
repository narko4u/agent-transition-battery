import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_perfect_square  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert not is_perfect_square(10)
        assert is_perfect_square(36)
        assert not is_perfect_square(14)
        assert is_perfect_square(14*14)
        assert not is_perfect_square(125)
        assert is_perfect_square(125*125)


if __name__ == "__main__":
    unittest.main()
