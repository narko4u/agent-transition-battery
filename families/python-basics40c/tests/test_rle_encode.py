import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import rle_encode


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(rle_encode("aaabb"), "a3b2")

    def test_case_2(self):
        self.assertEqual(rle_encode("abc"), "a1b1c1")

    def test_case_3(self):
        self.assertEqual(rle_encode(""), "")

    def test_case_4(self):
        self.assertEqual(rle_encode("a"), "a1")


if __name__ == "__main__":
    unittest.main()
