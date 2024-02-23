# Basic Concepts - 5 question
# Data types, evaluation (kiertekeles) - 6 question
# Control flow - 6 question
# Data - List, Tuple, Dict - 7 question
# Functions and exceptions - 6 question

# Task 1-2
print("Welcome", 'to', "Lsc", sep=', ', end='\n___________\n')
print("You are welcomed here")

a = 42  # type: int
b = "Apple"  # type: str
c = True  # bool or boolean

print(a, b, c)

# int() | str()
print(str(a) + " " + b + " " + str(c))
print(f'{a} {b} {c}')

# Task 3
print(type(a))
print(type(b))
print(type(c).__name__)

# Task 4 - Integers

print(123)
print(0o123)
print(0x123)
print(bin(123))
print(0b101101)

# Task 5 - Floats
aa = 0.0002
bb = 2e-4
print(aa)
print(bb)
print(0.000000000000000000000000000001)

# Task 6 - Spec chars
print("""
Dear sir madame,

Thanks broo you're the beeesttt.

"This is a famous quote";
""")

# Task 7 - Operators
try:
    aaa = int(input("First num: "))
    bbb = int(input("Second num: "))
    
    if aaa > bbb:
        print(f'a={aaa} is greater then b={bbb}')
    elif aaa < bbb:
        print(f'a={aaa} is less then b={bbb}')
    else:
        print(f'a={aaa} and b={bbb} are equal')
except:
    print("Error")


# Task 8 - Priorities
print(5 * 25 % 8 + 100 / 2 * 8 // 2)
print(5 * 25 % (8 + 100 / 2 * 8 // 2))

# Task 9 - Brackets
print(3 + 20 % 4 ** 2 * 5 / 5 - 5)
print((3 + (((20 % (4 ** 2)) * 5) / 5)) - 5)

# Task 10 - Random division Error
import random
try: 
    for i in range(1, 10):
        a1 = random.randint(-10, 10)
        a2 = random.randint(-10, 10)
        a3 = random.randint(-10, 10)
        a4 = random.randint(-10, 10)
        a5 = random.randint(-10, 10)
        a6 = random.randint(-10, 10)
        a7 = random.randint(-10, 10)
        print(a1/a2/a3/a4)
except ZeroDivisionError:
    print("At least one variable was zero")


