import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import human_bytes


class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(human_bytes(999), "999 B")
        self.assertEqual(human_bytes(1000), "1 KB")
        self.assertEqual(human_bytes(1500), "1.5 KB")
        self.assertEqual(human_bytes(1000000), "1 MB")


if __name__ == "__main__":
    unittest.main()
