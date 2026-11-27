import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import initials


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(initials("Ada Lovelace"), "A.L.")
        self.assertEqual(initials("grace"), "G.")
        self.assertEqual(initials(""), "")


if __name__ == "__main__":
    unittest.main()
