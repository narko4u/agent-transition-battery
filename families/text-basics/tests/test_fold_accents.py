import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import fold_accents


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(fold_accents("café"), "cafe")
        self.assertEqual(fold_accents("naïve résumé"), "naive resume")
        self.assertEqual(fold_accents("plain"), "plain")
        self.assertEqual(fold_accents(""), "")


if __name__ == "__main__":
    unittest.main()
