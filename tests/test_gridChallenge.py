import unittest
from hackerrank.gridChallenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge_example1(self):
        input_grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = "YES"
        self.assertEqual(gridChallenge(input_grid), expected_output)

    def test_grid_challenge_example2(self):
        input_grid = ['abc', 'def', 'ghi']
        expected_output = "YES"
        self.assertEqual(gridChallenge(input_grid), expected_output)

    def test_grid_challenge_single_row(self):
        input_grid = ["abc"]
        expected_output = "YES"
        self.assertEqual(gridChallenge(input_grid), expected_output)

    def test_grid_challenge_single_column(self):
        input_grid = ["a", "b", "c"]
        expected_output = "YES"
        self.assertEqual(gridChallenge(input_grid), expected_output)