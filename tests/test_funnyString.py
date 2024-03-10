import unittest
from unittest.mock import patch
from hackerrank.funnyString import funnyString

class TestFunnyString(unittest.TestCase):
    @patch('builtins.input', side_effect=["acxz"])
    def test_funny_string_acxz(self, mock_input):
        expected_output = "Funny"
        self.assertEqual(funnyString(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["bcxz"])
    def test_funny_string_bcxz(self, mock_input):
        expected_output = "Not Funny"
        self.assertEqual(funnyString(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["ptvzstvotxqyvzrwyqryzrpkswzryupwutmigc"])
    def test_funny_string_abcd(self, mock_input):
        expected_output = "Funny"
        self.assertEqual(funnyString(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["ceiosyrtztvnqsuozrxvtqywqwyrxtnjh"])
    def test_funny_string_abc(self, mock_input):
        expected_output = "Not Funny"
        self.assertEqual(funnyString(mock_input()), expected_output)
