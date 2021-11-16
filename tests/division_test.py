"""Testing Division"""
import unittest
from calc.calculations.division import Division

class ATestCase(unittest.TestCase):
    """Unit Test Class"""

    def setUp(self):
        self.calc = None

    def my_set_up(self, mynumbers):
        """Setup function"""
        self.calc = Division(mynumbers)

    def test_calculation_division(self):
        """testing that our calculator has a static method for division"""
        #Arrange
        mynumbers = (1.0, 2.0, 0.0)
        self.my_set_up(mynumbers)
        #Act
        #Assert
        assert self.calc.get_result() == 0.5
        #After we get result 0.5, it is divided by 0, it should throw ZeroDivisionError
        assert self.assertRaises(ZeroDivisionError)
