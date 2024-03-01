
myList = ["apple", "orange", "pear"]
myMatrix = [
    [1,2,3], 
    [2,3,4], 
    [3,4,5]
]
myTuple = (55, 66, 77)
myDict = { "first": 1, "second": 2}

# Variables
myString = "Losgiscool"
myBool = True
myInt = 45
myFloat = 3.14

# Task: Print data
print(myString)
for i in myString:
    print(i, end='')
print()

for i in myList:
    print(i, end=' ')
print()

for row in myMatrix:
    for col in row:
        print(col, end=' ')
    print()

for i in myTuple:
    print(i, end=', ')
print()

for key in myDict.keys():
    print(f'{key}: {myDict[key]}')

# Task: Mutable vs immutable
myList[0] = 10

