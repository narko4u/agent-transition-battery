import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import reverse_string_list  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
        assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
        assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']


if __name__ == "__main__":
    unittest.main()
