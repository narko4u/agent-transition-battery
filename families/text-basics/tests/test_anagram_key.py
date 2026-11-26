import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import anagram_key


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(anagram_key("Listen"), "eilnst")
        self.assertEqual(anagram_key("silent"), "eilnst")
        self.assertEqual(anagram_key("a1b!"), "ab")
        self.assertEqual(anagram_key(""), "")


if __name__ == "__main__":
    unittest.main()
