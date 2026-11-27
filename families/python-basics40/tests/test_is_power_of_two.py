import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import is_power_of_two


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_power_of_two(1), True)
        self.assertEqual(is_power_of_two(64), True)
        self.assertEqual(is_power_of_two(0), False)
        self.assertEqual(is_power_of_two(-4), False)
        self.assertEqual(is_power_of_two(6), False)


if __name__ == "__main__":
    unittest.main()
