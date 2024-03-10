import unittest
from hackerrank.alternate import alternate

class TestAlternate(unittest.TestCase):
    def test_alternate_example1(self):
        input_string = "beabeefeab"
        expected_output = 5
        self.assertEqual(alternate(input_string), expected_output)

    def test_alternate_example2(self):
        input_string = "aaaabbbb"
        expected_output = 0
        self.assertEqual(alternate(input_string), expected_output)

    def test_alternate_example3(self):
        input_string = "abcde"
        expected_output = 2
        self.assertEqual(alternate(input_string), expected_output)

    def test_alternate_example4(self):
        input_string = "ababababab"
        expected_output = 10
        self.assertEqual(alternate(input_string), expected_output)  