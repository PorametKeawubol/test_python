import unittest
from hackerrank.alternatingCharacters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_alternating_characters_AAAA(self):
        input_string = "AAAA"
        expected_output = 3
        self.assertEqual(alternatingCharacters(input_string), expected_output)

    def test_alternating_characters_BBBBB(self):
        input_string = "BBBBB"
        expected_output = 4
        self.assertEqual(alternatingCharacters(input_string), expected_output)

    def test_alternating_characters_ABABABAB(self):
        input_string = "ABABABAB"
        expected_output = 0
        self.assertEqual(alternatingCharacters(input_string), expected_output)

    def test_alternating_characters_BABABA(self):
        input_string = "BABABA"
        expected_output = 0
        self.assertEqual(alternatingCharacters(input_string), expected_output)

    def test_alternating_characters_AAABBB(self):
        input_string = "AAABBB"
        expected_output = 4
        self.assertEqual(alternatingCharacters(input_string), expected_output)