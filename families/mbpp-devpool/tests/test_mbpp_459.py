import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_uppercase  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
        assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
        assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'


if __name__ == "__main__":
    unittest.main()
