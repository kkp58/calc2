"""This is test file for all CSV files"""
import datetime

import pandas as pd

from calc.absolutepath import absolutepath
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction


def test_calculator_functions_with_csv_file_input():
    """Method to test calculations"""
    # results = open("allFunctionsResults.txt", "w", encoding='utf-8')

    with open("allFunctionsResults.txt", "w", encoding='utf-8') as results:

        #Addition
        results.write("Time Stamp:" + str(datetime.datetime.now()) + " Operation Addition\n")
        results.write('Record Value 1, Value 2, Result \n')
        test_data = pd.read_csv(absolutepath("tests/test_data/addition.csv"))
        for record, row in test_data.iterrows():
            add = Addition((row['Value 1'], row['Value 2']))
            assert round(add.get_result(),4) == round(row['Result'],4)
            results.write(
                str(record) + " " + str(row['Value 1']) + " , "
                + str(row['Value 2']) + " , " + str(add.get_result()))
            results.write("\n")
        results.write("\n \n")

        #Subtraction
        results.write("Time Stamp:" + str(datetime.datetime.now()) + " Operation Subtraction\n")
        results.write('Record Value 1, Value 2, Result \n')
        test_data = pd.read_csv(absolutepath("tests/test_data/subtraction.csv"))
        for record, row in test_data.iterrows():
            sub = Subtraction((row['Value 1'], row['Value 2']))
            assert round(sub.get_result(),4) == round(row['Result'],4)
            results.write(
                str(record) + " " + str(row['Value 1']) + " , " +
                str(row['Value 2']) + " , " + str(sub.get_result()))
            results.write("\n")
        results.write("\n \n")

        #Multiplication
        results.write("Time Stamp:" + str(datetime.datetime.now()) + " Operation Multiplication\n")
        results.write('Record Value 1, Value 2, Result \n')
        test_data = pd.read_csv(absolutepath("tests/test_data/multiplication.csv"))
        for record, row in test_data.iterrows():
            mul = Multiplication((row['Value 1'], row['Value 2']))
            assert round(mul.get_result(),4) == round(row['Result'],4)
            results.write(
                str(record) + " " + str(row['Value 1']) + " , "
                + str(row['Value 2']) + " , " + str(mul.get_result()))
            results.write("\n")
        results.write("\n \n")

        #Division
        results.write("Time Stamp:" + str(datetime.datetime.now()) + " Operation Division\n")
        results.write('Record Value 1, Value 2, Result \n')
        test_data = pd.read_csv(absolutepath("tests/test_data/division.csv"))
        for record, row in test_data.iterrows():
            divide = Division((row['Value 1'], row['Value 2']))
            results.write(
                str(record) + " " + str(row['Value 1']) + " , "
                + str(row['Value 2']) + " , " + str(divide.get_result()))
            results.write("\n")
        results.write("\n \n")
