import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import fizzbuzz_list


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fizzbuzz_list(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_case_2(self):
        self.assertEqual(fizzbuzz_list(15)[-1], "FizzBuzz")

    def test_case_3(self):
        self.assertEqual(fizzbuzz_list(0), [])


if __name__ == "__main__":
    unittest.main()
