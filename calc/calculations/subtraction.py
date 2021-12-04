"""Subtraction Class"""

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        difference_of_values = self.values[0] - self.values[1]
        return difference_of_values
