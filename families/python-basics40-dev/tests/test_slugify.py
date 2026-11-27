import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import slugify


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  A  B  "), "a-b")
        self.assertEqual(slugify("Café Olé"), "caf-ol")
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
