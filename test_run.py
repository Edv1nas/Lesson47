from main import covert_int_to_roman
import unittest


class TestConvertIntToRoman(unittest.TestCase):
    def test_convert_five_correctly(self):
        self.assertEqual(covert_int_to_roman(5), "V")

    def test_convert_nine_correctly(self):
        self.assertEqual(covert_int_to_roman(9), "IX")

    def test_convert_fourty_correctly(self):
        self.assertEqual(covert_int_to_roman(40), "XL")

    def test_convert_one_nine_zero_four_correctly(self):
        self.assertEqual(covert_int_to_roman(1904), "MCMIV")
