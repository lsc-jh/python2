import csv
import pandas as pd

desired_width = 320
pd.set_option("display.width", desired_width)
pd.set_option("display.max_columns", 10)

def openCSV():
    csvFile = pd.read_csv("oscar_age_female.csv")
    print(csvFile.head(20))
openCSV()

def openColumns():
    csvFile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    print(csvFile.head(10))
    summ = csvFile["Age"].sum()
    rows = len(csvFile["Age"])
    avg = summ / rows
    print(summ)
    print(f"Az atlag kor: {avg}")
openColumns()


def oldestWinner():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Age", "Name"])
    max_age = max(csvfile["Age"])
    myRow = csvfile[csvfile["Age"] == max_age]
    print("The oldest winner is " + str(myRow.iloc[0, 0]) + " years old and she is" + str(myRow.iloc[0, 1]).replace("\"",""))
oldestWinner()


def fargoWin():
    csvfile = pd.read_csv("oscar_age_female.csv", usecols=["Year", "Movie"], skipinitialspace=True)
    myRow = csvfile[csvfile["Movie"] == "Fargo"]
    print(str(myRow.iloc[0, 1]) + " won the Oscar in " + str(myRow.iloc[0, 0]))
fargoWin()


def dataRow(row):
    csvfile = pd.read_csv("oscar_age_female.csv")
    myRow = csvfile.iloc[row]
    print(myRow)
dataRow(5)

