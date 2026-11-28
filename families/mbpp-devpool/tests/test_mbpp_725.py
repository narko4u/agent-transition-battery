import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import *  # noqa: F401,F403
from solution import extract_quotation  # noqa: F401



class TestCase(unittest.TestCase):
    def test_cases(self):
        assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
        assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
        assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
        assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []


if __name__ == "__main__":
    unittest.main()
