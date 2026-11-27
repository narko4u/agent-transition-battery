import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_power_of_two


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(is_power_of_two(1), True)

    def test_case_2(self):
        self.assertEqual(is_power_of_two(64), True)

    def test_case_3(self):
        self.assertEqual(is_power_of_two(0), False)

    def test_case_4(self):
        self.assertEqual(is_power_of_two(-4), False)

    def test_case_5(self):
        self.assertEqual(is_power_of_two(6), False)


if __name__ == "__main__":
    unittest.main()
