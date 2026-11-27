import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import rle_decode


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(rle_decode("a3b2"), "aaabb")

    def test_case_2(self):
        self.assertEqual(rle_decode(""), "")

    def test_case_3(self):
        self.assertEqual(rle_decode("a1"), "a")

    def test_case_4(self):
        with self.assertRaises(ValueError):
            rle_decode("a0")


if __name__ == "__main__":
    unittest.main()
