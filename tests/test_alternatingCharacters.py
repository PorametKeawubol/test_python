import unittest
from unittest.mock import patch
from hackerrank.alternatingCharacters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    @patch('builtins.input', side_effect=["AAAA"])
    def test_alternating_characters_AAAA(self, mock_input):
        expected_output = 3
        self.assertEqual(alternatingCharacters(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["BBBBB"])
    def test_alternating_characters_BBBBB(self, mock_input):
        expected_output = 4
        self.assertEqual(alternatingCharacters(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["ABABABAB"])
    def test_alternating_characters_ABABABAB(self, mock_input):
        expected_output = 0
        self.assertEqual(alternatingCharacters(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["BABABA"])
    def test_alternating_characters_BABABA(self, mock_input):
        expected_output = 0
        self.assertEqual(alternatingCharacters(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["AAABBB"])
    def test_alternating_characters_AAABBB(self, mock_input):
        expected_output = 4
        self.assertEqual(alternatingCharacters(mock_input()), expected_output)