"""Testing the Calculator"""
import pprint

import unittest

from calculator.calculator import Calculator

class ATestCase(unittest.TestCase):
    """Unit Test Class"""
    #a function that will run each time you pass it to a test, it is called a fixture
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        self.calc.clear_history()

    def test_calculator_add(self):
        """Testing the Add function of the calculator"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.add_number(1,2) == 3
        assert self.calc.add_number(2, 2) == 4
        assert self.calc.history_count() == 2
        assert self.calc.get_result_of_last_calculation_added_to_history() == 4
        pprint.pprint(Calculator.history)

    def test_clear_history(self):
        """Testing clear history function"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.add_number(1,2) == 3
        assert self.calc.add_number(2, 2) == 4
        assert self.calc.history_count() == 2
        assert self.calc.clear_history() is True
        assert self.calc.history_count() == 0

    def test_count_history(self):
        """Testing history's count function"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.history_count() == 0
        assert self.calc.add_number(2, 2) == 4
        assert self.calc.add_number(3, 2) == 5
        assert self.calc.history_count() == 2

    def test_get_last_calculation_result(self):
        """Testing the last calculation result stored"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.add_number(2, 2) == 4
        assert self.calc.add_number(3, 2) == 5
        assert self.calc.get_result_of_last_calculation_added_to_history() == 5

    def test_get_first_calculation_result(self):
        """Testing the first calculation result stored"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.add_number(2, 2) == 4
        assert self.calc.add_number(3, 2) == 5
        assert self.calc.get_result_of_first_calculation_added_to_history() == 4

    def test_calculator_subtract(self):
        """Testing the subtract method of the calculator"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.subtract_number(1, 2) == -1

    def test_calculator_multiply(self):
        """ tests multiplication of two numbers"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.multiply_numbers(1,2) == 2

    def test_calculator_divide(self):
        """ tests division of two numbers"""
        # pylint: disable=unused-argument,redefined-outer-name
        assert self.calc.divide_numbers(10, 2) == 5

    def test_calculator_zero_divide(self):
        """ tests division by zeros"""
        # pylint: disable=unused-argument,redefined-outer-name
        self.calc.divide_numbers(10,0)
        self.assertRaises(ZeroDivisionError)
