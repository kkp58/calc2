"""Testing the Calculator"""
import unittest

from calculator.main import Calculator
class ATestCase(unittest.TestCase):
    """Test case class"""
    def setUp(self):
        """Setting up initial calc"""
        self.calc = Calculator()
    def test_calculator_result(self):
        """testing calculator result is 0"""
        assert self.calc.result == 0

    def test_calculator_add(self):
        """Testing the Add function of the calculator"""
        #Act by calling the method to be tested
        self.calc.add_number(4)
        #Assert that the results are correct
        assert self.calc.result == 4

    def test_calculator_get_result(self):
        """Testing the Get result method of the calculator"""
        assert self.calc.get_result() == 0

    def test_calculator_subtract(self):
        """Testing the subtract method of the calculator"""
        # calc = Calculator()
        self.calc.subtract_number(1)
        assert self.calc.get_result() == -1

    def test_calculator_multiply(self):
        """ tests multiplication of two numbers"""
        self.calc.multiply_numbers(1,2)
        assert self.calc.result == 2

    def test_calculator_divide(self):
        """ tests division of two numbers"""
        self.calc.divide_number(10, 2)
        assert self.calc.result == 5

    def test_calculator_zero_divide(self):
        """ tests division by zeros"""
        self.calc.divide_number(10, 0)
        self.assertRaises(ZeroDivisionError)
