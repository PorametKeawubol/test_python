import unittest
from unittest.mock import patch
from hackerrank.caesarCipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    @patch('builtins.input', side_effect=["middle-Outz", 2])
    def test_caesar_cipher_example1(self, mock_input):
        expected_output = "okffng-Qwvb"
        self.assertEqual(caesarCipher(mock_input()[0], mock_input()[1]), expected_output)

    @patch('builtins.input', side_effect=["middle-Outz", 26])
    def test_caesar_cipher_example2(self, mock_input):
        expected_output = "middle-Outz"
        self.assertEqual(caesarCipher(mock_input()[0], mock_input()[1]), expected_output)

    @patch('builtins.input', side_effect=["Hello_World!", 10])
    def test_caesar_cipher_example3(self, mock_input):
        expected_output = "Rovvy_Gybvn!"
        self.assertEqual(caesarCipher(mock_input()[0], mock_input()[1]), expected_output)

    @patch('builtins.input', side_effect=["Always-Look-on-the-Bright-Side-of-Life", 5])
    def test_caesar_cipher_example4(self, mock_input):
        expected_output = "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
        self.assertEqual(caesarCipher(mock_input()[0], mock_input()[1]), expected_output)
        
        