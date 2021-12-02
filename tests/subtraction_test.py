import unittest
import pandas as pd


from calc.calculations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = None

    def my_set_up(self):
        """Setup function"""
        self.calc = Subtraction()

    def test_subtraction(self):
        additionResult = open("additionResult.txt", "w")
        additionResult.write('Value 1, Value 2, Result')
        test_data = pd.read_csv("tests/test_data/subtraction.csv")
        for idx, row in test_data.iterrows():
            result = float(row['Result'])
            x = self.calc.get_result(row['Value 1'], row['Value 2'])
            additionResult.write(row['Value 1'] + row['Value 2'] + x)
            self.assertEqual(self.calc.get_result(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calc.result, result)
        additionResult.close()

if __name__ == '__main__':
    unittest.main()
