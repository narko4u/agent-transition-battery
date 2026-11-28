import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import concatenate_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
        assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
        assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'


if __name__ == "__main__":
    unittest.main()
