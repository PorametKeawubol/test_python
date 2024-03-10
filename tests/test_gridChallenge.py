import unittest
from unittest.mock import patch
from hackerrank.gridChallenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 'ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
    def test_grid_challenge_example1(self, mock_input):
        expected_output = "YES"
        self.assertEqual(gridChallenge(mock_input()), expected_output)

    @patch('builtins.input', side_effect=[3, 'abc', 'def', 'ghi'])
    def test_grid_challenge_example2(self, mock_input):
        expected_output = "YES"
        self.assertEqual(gridChallenge(mock_input()), expected_output)

    @patch('builtins.input', side_effect=[1, 'abc'])
    def test_grid_challenge_single_row(self, mock_input):
        expected_output = "YES"
        self.assertEqual(gridChallenge(mock_input()), expected_output)

    @patch('builtins.input', side_effect=[3, 'a', 'b', 'c'])
    def test_grid_challenge_single_column(self, mock_input):
        expected_output = "YES"
        self.assertEqual(gridChallenge(mock_input()), expected_output)