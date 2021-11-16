"""Division Class"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            try:
                result = result / value
            except ZeroDivisionError:
                print("Cannot divide by zero")
        return result
