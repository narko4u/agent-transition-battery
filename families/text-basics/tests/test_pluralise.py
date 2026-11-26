import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import pluralise


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(pluralise("cat"), "cats")
        self.assertEqual(pluralise("bus"), "buses")
        self.assertEqual(pluralise("city"), "cities")
        self.assertEqual(pluralise("key"), "keys")


if __name__ == "__main__":
    unittest.main()
