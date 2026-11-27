import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import caesar


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesar("abc", 1), "bcd")

    def test_case_2(self):
        self.assertEqual(caesar("XYZ", 2), "ZAB")

    def test_case_3(self):
        self.assertEqual(caesar("a-b!", 3), "d-e!")

    def test_case_4(self):
        self.assertEqual(caesar("abc", -1), "zab")


if __name__ == "__main__":
    unittest.main()
