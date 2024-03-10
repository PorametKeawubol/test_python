import unittest
from hackerrank.funnyString import funnyString

class TestFunnyString(unittest.TestCase):
    def test_funny_string_acxz(self):
        input_string = "acxz"
        expected_output = "Funny"
        self.assertEqual(funnyString(input_string), expected_output)

    def test_funny_string_bcxz(self):
        input_string = "bcxz"
        expected_output = "Not Funny"
        self.assertEqual(funnyString(input_string), expected_output)

    def test_funny_string_abcd(self):
        input_string = "ptvzstvotxqyvzrwyqryzrpkswzryupwutmigc"
        expected_output = "Funny"
        self.assertEqual(funnyString(input_string), expected_output)

    def test_funny_string_abc(self):
        input_string = "ceiosyrtztvnqsuozrxvtqywqwyrxtnjh"
        expected_output = "Not Funny"
        self.assertEqual(funnyString(input_string), expected_output)

