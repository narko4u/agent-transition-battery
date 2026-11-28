import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import remove_length  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert remove_length('The person is most value tet', 3) == 'person is most value'
        assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
        assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'


if __name__ == "__main__":
    unittest.main()
