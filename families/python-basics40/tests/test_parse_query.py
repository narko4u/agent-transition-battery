import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import parse_query


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(parse_query("a=1&b=2&a=3"), {'a': '3', 'b': '2'})
        self.assertEqual(parse_query("q=hello+world"), {'q': 'hello world'})
        self.assertEqual(parse_query("flag"), {'flag': ''})
        self.assertEqual(parse_query(""), {})


if __name__ == "__main__":
    unittest.main()
