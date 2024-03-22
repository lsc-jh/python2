# Task 1: While loop
myNum = int(input("Enter a number: "))
while myNum > 1:
    if myNum % 3 == 0:
        myNum /= 3
    else:
        myNum += 1
    print(myNum)
print(myNum)

# Task 2: While true
boolean = True
i = 0
while boolean:
    print(i)
    i += 1
    if i == 50000:
        boolean = False

# Task 2.1: While true without variable
i = 0
while not i == 50000:
    print(i)
    i += 1

# Task 3: While list
myList = ["dog", "cat", "bird", "fish"]
i = 0
while i < len(myList):
    print(myList[i])
    i += 1



