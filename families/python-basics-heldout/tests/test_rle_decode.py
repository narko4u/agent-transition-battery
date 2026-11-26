import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import rle_decode


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(rle_decode("a3b2"), "aaabb")
        self.assertEqual(rle_decode(""), "")
        self.assertEqual(rle_decode("a1"), "a")
        with self.assertRaises(ValueError):
            rle_decode("a0")


if __name__ == "__main__":
    unittest.main()
