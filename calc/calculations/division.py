"""Division Class"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        try:
            result = self.value_a/self.value_b
        except ZeroDivisionError:
            err_name = "ZeroDivisionError"
            return err_name
        return result
