import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import replace_specialchar  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
        assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
        assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')


if __name__ == "__main__":
    unittest.main()
