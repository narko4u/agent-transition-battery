import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import interleave


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(interleave([1, 2, 3], ["a", "b"]), [1, 'a', 2, 'b', 3])
        self.assertEqual(interleave([], [1, 2]), [1, 2])
        self.assertEqual(interleave([], []), [])


if __name__ == "__main__":
    unittest.main()
