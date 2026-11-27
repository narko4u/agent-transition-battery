import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import tuple_size  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
        assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu") ) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
        assert tuple_size(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))  ) == sys.getsizeof(((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf")))


if __name__ == "__main__":
    unittest.main()
