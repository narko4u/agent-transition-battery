import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import transpose


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_case_2(self):
        self.assertEqual(transpose([]), [])

    def test_case_3(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_case_4(self):
        with self.assertRaises(ValueError):
            transpose([[1, 2], [3]])


if __name__ == "__main__":
    unittest.main()
