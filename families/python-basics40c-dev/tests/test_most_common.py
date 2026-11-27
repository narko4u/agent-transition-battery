import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import most_common


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(most_common([1, 2, 2, 3]), 2)

    def test_case_2(self):
        self.assertEqual(most_common(["a", "b", "b", "a"]), "a")

    def test_case_3(self):
        self.assertEqual(most_common([9]), 9)

    def test_case_4(self):
        with self.assertRaises(ValueError):
            most_common([])


if __name__ == "__main__":
    unittest.main()
