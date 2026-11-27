import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import clamp


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(clamp(5, 1, 10), 5)
        self.assertEqual(clamp(-5, 1, 10), 1)
        self.assertEqual(clamp(50, 1, 10), 10)
        with self.assertRaises(ValueError):
            clamp(1, 5, 2)


if __name__ == "__main__":
    unittest.main()
