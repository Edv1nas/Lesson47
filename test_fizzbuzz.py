import unittest
from exercise_fizz import fizzbuzz


class TestConvertIntToRoman(unittest.TestCase):
    def test_fizzbuzz_division_by_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_fizzbuzz_division_by_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz_division_by_five_and_three(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
