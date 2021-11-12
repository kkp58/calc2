"""This is subtraction inherits the value A and value B from the calculation class"""


from calc.calculation import Calculation

#This is how you extend the Subtraction class with the Calculation
class Subtraction(Calculation):
    """The subtraction class has one method to get the result of the the calculation A and B come
    from the calculation parent class"""
    def get_result(self):
        """This is encapsulation"""
        return self.value_a - self.value_b
