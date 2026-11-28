import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import start_withp  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
        assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
        assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')


if __name__ == "__main__":
    unittest.main()
