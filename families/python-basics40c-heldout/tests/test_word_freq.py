import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import word_freq


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(word_freq("The cat the dog", 2), [('the', 2), ('cat', 1)])

    def test_case_2(self):
        self.assertEqual(word_freq("b a b a c", 3), [('a', 2), ('b', 2), ('c', 1)])

    def test_case_3(self):
        self.assertEqual(word_freq("", 5), [])

    def test_case_4(self):
        self.assertEqual(word_freq("a", 0), [])


if __name__ == "__main__":
    unittest.main()
