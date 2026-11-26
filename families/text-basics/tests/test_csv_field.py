import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import csv_field


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(csv_field("plain"), "plain")
        self.assertEqual(csv_field("a,b"), "\"a,b\"")
        self.assertEqual(csv_field('he said "hi"'), "\"he said \"\"hi\"\"\"")
        self.assertEqual(csv_field("a\nb"), "\"a\nb\"")


if __name__ == "__main__":
    unittest.main()
