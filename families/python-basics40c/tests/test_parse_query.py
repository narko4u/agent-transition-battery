import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import parse_query


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(parse_query("a=1&b=2&a=3"), {'a': '3', 'b': '2'})

    def test_case_2(self):
        self.assertEqual(parse_query("q=hello+world"), {'q': 'hello world'})

    def test_case_3(self):
        self.assertEqual(parse_query("flag"), {'flag': ''})

    def test_case_4(self):
        self.assertEqual(parse_query(""), {})


if __name__ == "__main__":
    unittest.main()
