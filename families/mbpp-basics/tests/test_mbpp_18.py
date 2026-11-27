import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import str_to_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
        assert remove_dirty_chars("digitalindia", "talent") == 'digiidi'
        assert remove_dirty_chars("exoticmiles", "toxic") == 'emles'


if __name__ == "__main__":
    unittest.main()
