import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import parse_kv


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(parse_kv("a=1; b=2"), {'a': '1', 'b': '2'})
        self.assertEqual(parse_kv("a=1; a=2"), {'a': '2'})
        self.assertEqual(parse_kv(""), {})
        with self.assertRaises(ValueError):
            parse_kv("a=1; broken")


if __name__ == "__main__":
    unittest.main()
