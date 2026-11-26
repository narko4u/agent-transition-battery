import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_palindrome


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(is_palindrome("abc"), False)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("Never odd or even"), True)


if __name__ == "__main__":
    unittest.main()
