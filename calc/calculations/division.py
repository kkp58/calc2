"""Division Class"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        try:
            result = self.values[0]/self.values[1]
        except ZeroDivisionError:
            err_name = "ZeroDivisionError"
            return err_name
        return result
