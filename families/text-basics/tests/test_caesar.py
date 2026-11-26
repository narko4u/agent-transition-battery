import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import caesar


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(caesar("Abc xyz", 2), "Cde zab")
        self.assertEqual(caesar("abc", -1), "zab")
        self.assertEqual(caesar("Hello, World!", 0), "Hello, World!")
        self.assertEqual(caesar("z", 1), "a")


if __name__ == "__main__":
    unittest.main()
