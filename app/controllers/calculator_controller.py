"""Calculator controller class"""
from flask import Flask
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase


from calc.calculator import Calculator

app = Flask(__name__)

class CalculatorController(ControllerBase):
    """"Extends base controller class"""
    @staticmethod
    def post():
        """Post method to get calculations done"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must need to enter a number for value 1 or value 2'
        else:
            flash('Your calculation is done successfully')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            Calculator.write_to_csv(value1 , value2, result, operation)
            return render_template('result.html', value1=value1, value2=value2,
                                   operation=operation, result=result)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        """getting calculator template"""
        return render_template('calculator.html')
