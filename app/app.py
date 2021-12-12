"""A simple flask web app"""
from flask import Flask
from app.controllers.calculator_controller import CalculatorController
from app.controllers.table_controller import TableController
from flask import render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/table", methods = ['GET'])
def table_get_post():
    return TableController.get()

@app.route("/history", methods = ['GET'])
def history_page():
    return render_template("history.html")

@app.route("/AAATesting", methods = ['GET'])
def aaa_page():
    return render_template("AAATesting.html")

@app.route("/design", methods = ['GET'])
def design_page():
    return render_template("design.html")

@app.route("/pylintAndOthers", methods = ['GET'])
def pylint():
    return render_template("pylintAndOthers.html")