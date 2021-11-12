"""This is the division calculation inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation

#This is how you extend the Division class with the Calculation
class Division(Calculation):
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        """This is encapsulation"""
        result = 0
        try:
            result = self.value_a / self.value_b
        except ZeroDivisionError:
            print("Cannot divide by zero")
        return result
