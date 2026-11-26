import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import title_case


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(title_case("the lord of the rings"), "The Lord of the Rings")
        self.assertEqual(title_case("a tale of two cities"), "A Tale of Two Cities")
        self.assertEqual(title_case("WAR AND PEACE"), "War and Peace")
        self.assertEqual(title_case(""), "")


if __name__ == "__main__":
    unittest.main()
