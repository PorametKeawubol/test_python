import unittest
from unittest.mock import patch
from number_utils.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):
    @patch('number_utils.number_utils.is_prime_list', return_value=True)
    def test_prime_list_1_2_3_is_prime(self, mock_is_prime_list):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    @patch('number_utils.number_utils.is_prime_list', return_value=False)
    def test_prime_list_4_6_8_is_not_prime(self, mock_is_prime_list):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    @patch('number_utils.number_utils.is_prime_list', return_value=True)
    def test_prime_list_5_7_11_is_prime(self, mock_is_prime_list):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)