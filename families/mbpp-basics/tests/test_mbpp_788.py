import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import new_tuple  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
        assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
        assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')


if __name__ == "__main__":
    unittest.main()
