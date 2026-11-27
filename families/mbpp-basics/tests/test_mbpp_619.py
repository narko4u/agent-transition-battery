import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import move_num  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
        assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
        assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'


if __name__ == "__main__":
    unittest.main()
