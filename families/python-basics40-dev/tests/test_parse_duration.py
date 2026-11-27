import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import parse_duration


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(parse_duration("1h30m45s"), 5445)
        self.assertEqual(parse_duration("90s"), 90)
        self.assertEqual(parse_duration("2m"), 120)
        self.assertEqual(parse_duration(""), 0)
        with self.assertRaises(ValueError):
            parse_duration("1x")


if __name__ == "__main__":
    unittest.main()
