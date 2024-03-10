import unittest
from hackerrank.caesarCipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_caesar_cipher_example1(self):
        input_string = "middle-Outz"
        rotation_factor = 2
        expected_output = "okffng-Qwvb"
        self.assertEqual(caesarCipher(input_string, rotation_factor), expected_output)

    def test_caesar_cipher_example2(self):
        input_string = "middle-Outz"
        rotation_factor = 26
        expected_output = "middle-Outz"
        self.assertEqual(caesarCipher(input_string, rotation_factor), expected_output)

    def test_caesar_cipher_example3(self):
        input_string = "Hello_World!"
        rotation_factor = 10
        expected_output = "Rovvy_Gybvn!"
        self.assertEqual(caesarCipher(input_string, rotation_factor), expected_output)

    def test_caesar_cipher_example4(self):
        input_string = "Always-Look-on-the-Bright-Side-of-Life"
        rotation_factor = 5
        expected_output = "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
        self.assertEqual(caesarCipher(input_string, rotation_factor), expected_output)

        
        