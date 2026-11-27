import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import snake_case


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(snake_case("Hello, World!"), "hello_world")

    def test_case_2(self):
        self.assertEqual(snake_case("  A  B "), "a_b")

    def test_case_3(self):
        self.assertEqual(snake_case(""), "")

    def test_case_4(self):
        self.assertEqual(snake_case("already_snake"), "already_snake")


if __name__ == "__main__":
    unittest.main()
