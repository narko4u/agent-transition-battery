import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import mode_value


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(mode_value([1, 2, 2, 3]), 2)

    def test_case_2(self):
        self.assertEqual(mode_value([3, 1, 3, 1]), 1)

    def test_case_3(self):
        self.assertEqual(mode_value([7]), 7)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            mode_value([])


if __name__ == "__main__":
    unittest.main()
