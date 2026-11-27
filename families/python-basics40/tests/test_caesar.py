import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import caesar


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(caesar("abc", 1), "bcd")
        self.assertEqual(caesar("XYZ", 2), "ZAB")
        self.assertEqual(caesar("a-b!", 3), "d-e!")
        self.assertEqual(caesar("abc", -1), "zab")


if __name__ == "__main__":
    unittest.main()
