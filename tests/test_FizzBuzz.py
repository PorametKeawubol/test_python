from FizzBuzz.FizzBuzz import FizzBuzz
import unittest
class TestFizzBuzz(unittest.TestCase):
    def test_Fizz(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(6), "Fizz")
    def test_Buzz(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(10), "Buzz")
    
    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")
    
    def test_Normal(self):
        self.assertEqual(FizzBuzz(1), None)
        self.assertEqual(FizzBuzz(7), None)