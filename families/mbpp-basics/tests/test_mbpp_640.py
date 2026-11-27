import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_parenthesis  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_parenthesis(["python (chrome)"])==("python")
        assert remove_parenthesis(["string(.abc)"])==("string")
        assert remove_parenthesis(["alpha(num)"])==("alpha")


if __name__ == "__main__":
    unittest.main()
