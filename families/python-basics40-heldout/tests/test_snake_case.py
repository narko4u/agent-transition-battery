import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import snake_case


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(snake_case("Hello, World!"), "hello_world")
        self.assertEqual(snake_case("  A  B "), "a_b")
        self.assertEqual(snake_case(""), "")
        self.assertEqual(snake_case("already_snake"), "already_snake")


if __name__ == "__main__":
    unittest.main()
