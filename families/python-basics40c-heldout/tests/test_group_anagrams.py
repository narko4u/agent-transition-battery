import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import group_anagrams


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate"]), {'aet': ['ate', 'eat', 'tea'], 'ant': ['tan']})

    def test_case_2(self):
        self.assertEqual(group_anagrams([]), {})


if __name__ == "__main__":
    unittest.main()
