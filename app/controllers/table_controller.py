import os

from app.controllers.controller import ControllerBase
from flask import render_template
import pandas as pd


class TableController(ControllerBase):
    @staticmethod
    def get():
        if os.stat("result.csv").st_size == 0:
            return render_template('empty.html')
        else:
            df = pd.read_csv("result.csv", header=None)
            values = df.values.tolist()
            return render_template('table.html', values=values)