import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import second_largest


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(second_largest([1, 3, 2]), 2)

    def test_case_2(self):
        self.assertEqual(second_largest([5, 5, 4]), 4)

    def test_case_3(self):
        with self.assertRaises(ValueError):
            second_largest([7])

    def test_case_4(self):
        with self.assertRaises(ValueError):
            second_largest([2, 2, 2])


if __name__ == "__main__":
    unittest.main()
