"""
Author: Anjana Vasudevan
Objective - easily load datasets and the related info
"""

# necessary modules:
import pandas as pd
import numpy as np


class Dataser_loader(object):
    """
    Loads the dataframe and processes columns
    """

    def __init__(self, path):
        self.path = path

    def load(self):
        self.dataframe = pd.read_csv(self.path)

        # Print the data
        self.dataframe.head(10)
        print(f"Loading succesful")

    def display_column_info(self):
        for column in self.dataframe.columns:
            print(f"Field: {column} | type of data: {type(column)}")

        # Display no. of columns
        print(f"No. of columns: {len(self.dataframe.columns)}")
