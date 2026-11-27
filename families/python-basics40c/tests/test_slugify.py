import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import slugify


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_case_2(self):
        self.assertEqual(slugify("  A  B  "), "a-b")

    def test_case_3(self):
        self.assertEqual(slugify("Café Olé"), "caf-ol")

    def test_case_4(self):
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
