import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import ellipsize


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(ellipsize("hello world", 5), "hello...")
        self.assertEqual(ellipsize("hi", 5), "hi")
        self.assertEqual(ellipsize("abc def", 4), "abc...")
        self.assertEqual(ellipsize("", 3), "")


if __name__ == "__main__":
    unittest.main()
