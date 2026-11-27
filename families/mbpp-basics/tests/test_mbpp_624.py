import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import is_upper  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert is_upper("person") =="PERSON"
        assert is_upper("final") == "FINAL"
        assert is_upper("Valid") == "VALID"


if __name__ == "__main__":
    unittest.main()
