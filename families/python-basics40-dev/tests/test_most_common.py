import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import most_common


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(most_common([1, 2, 2, 3]), 2)
        self.assertEqual(most_common(["a", "b", "b", "a"]), "a")
        self.assertEqual(most_common([9]), 9)
        with self.assertRaises(ValueError):
            most_common([])


if __name__ == "__main__":
    unittest.main()
