import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import find_char_long  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
        assert set(find_char_long('Jing Eco and Tech')) == set(['Jing', 'Tech'])
        assert set(find_char_long('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])


if __name__ == "__main__":
    unittest.main()
