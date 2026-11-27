import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_palindrome


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)

    def test_case_2(self):
        self.assertEqual(is_palindrome("abc"), False)

    def test_case_3(self):
        self.assertEqual(is_palindrome(""), True)

    def test_case_4(self):
        self.assertEqual(is_palindrome("Never odd or even"), True)


if __name__ == "__main__":
    unittest.main()
