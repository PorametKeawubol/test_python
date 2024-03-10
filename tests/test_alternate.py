import unittest
from unittest.mock import patch
from hackerrank.alternate import alternate

class TestAlternate(unittest.TestCase):
    @patch('builtins.input', side_effect=["beabeefeab"])
    def test_alternate_example1(self, mock_input):
        expected_output = 5
        self.assertEqual(alternate(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["aaaabbbb"])
    def test_alternate_example2(self, mock_input):
        expected_output = 0
        self.assertEqual(alternate(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["abcde"])
    def test_alternate_example3(self, mock_input):
        expected_output = 2
        self.assertEqual(alternate(mock_input()), expected_output)

    @patch('builtins.input', side_effect=["ababababab"])
    def test_alternate_example4(self, mock_input):
        expected_output = 10
        self.assertEqual(alternate(mock_input()), expected_output)

if __name__ == '__main__':
    unittest.main()
