import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import initials


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(initials("Ada Lovelace"), "A.L.")

    def test_case_2(self):
        self.assertEqual(initials("grace"), "G.")

    def test_case_3(self):
        self.assertEqual(initials(""), "")


if __name__ == "__main__":
    unittest.main()
