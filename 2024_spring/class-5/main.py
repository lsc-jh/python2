
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
myList[0] = "asd"
print(myList)

# myTuple[0] = 34 # ERROR

# Task: Immutable int variable
print(myInt)
print(f'id: {id(myInt)}')
myInt = 100
print(myInt)
print(f'id: {id(myInt)}')

# Task: id of a list
print(f'id: {id(myList)}')
myList.append("ert")
myList[2] = "345"
print(f'id: {id(myList)}')

myTupleList = ([1,2,3], 3, 4)
print(myTupleList)
print(id(myTupleList))
myTupleList[0][0] = 10
print(myTupleList)
print(id(myTupleList))
myTupleList = tuple(list(myTupleList))
print(myTupleList)
print(id(myTupleList))

# Task: Clock time
seconds = int(input("Enter the seconds: "))
seconds = seconds % (24*3600)
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f'The exact time is: {hours}:{minutes}:{seconds}')

#Task List append
# Solution 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    list2.append(i**2)
print(list1)
print(list2)

# Solution 2
list2 = []
for i in range(0, len(list1)):
    list2.append(list1[i]**2)
print(list1)
print(list2)

# Task: Divisiblity
for i in range(1000, 2500):
    def dvdr(d):
        return i % d == 0

    def ndvdr(d):
        return not dvdr(d)

    # ==> => #{ @_ *** <== <| |> || //=
    if dvdr(7) and ndvdr(5) and ndvdr(2) and dvdr(3):
        print(i, end=",")
print()
