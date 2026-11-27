import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import transpose


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(transpose([]), [])
        self.assertEqual(transpose([[1]]), [[1]])
        with self.assertRaises(ValueError):
            transpose([[1, 2], [3]])


if __name__ == "__main__":
    unittest.main()
