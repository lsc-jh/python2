import csv
import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_columns", 10)

def openCSV():
    csvFile = pd.read_csv("oscar_age_female.csv")
    print(csvFile.head(20))
# openCSV()

def openColumns():
    csvFile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    print(csvFile.head(10))
    summ = csvFile["Age"].sum()
    rows = len(csvFile["Age"])
    avg = summ / rows
    print(summ)
    print(f"Az atlag kor: {avg}")


openColumns()
