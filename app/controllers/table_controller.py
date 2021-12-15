"""This is table controller file"""
import os
import pandas as pd
from flask import render_template
from app.controllers.controller import ControllerBase


class TableController(ControllerBase):
    """Class table controller"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def get():
        """to get the results"""
        if os.stat("result.csv").st_size == 0:
            return render_template('empty.html')
        else:
            record = pd.read_csv("result.csv", header=None)
            values = record.values.tolist()
            return render_template('table.html', values=values)
