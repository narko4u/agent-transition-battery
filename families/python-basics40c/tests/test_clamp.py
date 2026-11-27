import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import clamp


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(clamp(5, 1, 10), 5)

    def test_case_2(self):
        self.assertEqual(clamp(-5, 1, 10), 1)

    def test_case_3(self):
        self.assertEqual(clamp(50, 1, 10), 10)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            clamp(1, 5, 2)


if __name__ == "__main__":
    unittest.main()
