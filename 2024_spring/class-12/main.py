import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Task 1 - Read and print the contents of the file
def open_and_print():
    csvfile = open('deniro.csv', 'r')
    data = csv.reader(csvfile, skipinitialspace=True)
    for row in data:
        print(', '.join(row))
    csvfile.close()


# open_and_print()


# Task 2 - Read as Tables
def open_as_table():
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('deniro.csv', skipinitialspace=True, index_col='Year')
    print(data)


# open_as_table()


# Task 3 - Pick specific columns
def pick_columns(cols: list[str]):
    pd.set_option('display.max_rows', None)
    data = pd.read_csv('deniro.csv', skipinitialspace=True, usecols=cols)
    print(data)


# pick_columns(['Score', 'Title'])


# Task 4 - Get the column names
def get_column_names():
    data = pd.read_csv('deniro.csv', skipinitialspace=True)
    list_columns = list(data.columns)
    print(list_columns)


# get_column_names()


# Task 5 - Best Movie
def best_movie():
    data = pd.read_csv('deniro.csv', skipinitialspace=True)
    best_score = max(data['Score'])
    row = data[data['Score'] == best_score]
    iloc = row.iloc[0, 0]
    print(f"Best movie: {row.iloc}")


best_movie()

