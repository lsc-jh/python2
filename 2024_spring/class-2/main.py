from myerror import MyError


# Input error
value = int(input("enter an integer: "))
print(f'Half of {value} is {value / 2}')


value = input("enter an integer: ")
if value.isdecimal():
    value = int(value)
    print(f'Half of {value} is {value / 2}')
else:
    print("The input is not valid integer!")

print("Some stuff")

try:
    value = int(input("enter an integer: "))
    print(f'The reciprocal of {value} is {1/value}')
except:
    print("Oh noo, I can't do this!")

print("Some other stuff")


try:
    value = int(input("enter an integer: "))
    print(value/value)
except ValueError:
    print("Bad input!")
except ZeroDivisionError:
    print("Bad boy, you can't divide with zero")
except:
    print("Boo!")

def division(a, b):
    try:
        c = a / b
        print(f'{a} / {b} = {c}')
    except TypeError:
        print("One of the parameters are incorrect")
    except ZeroDivisionError:
        print("Bad boy, you can't divide with zero")
    else:
        print("well done")
division(0, 0)

try:
    f = open('test.txt', 'a+')
    try:
        f.write("Lorem ipsum")
    except:
        print("Writing the file went wrong!")
    finally:
        f.close()
except:
    print("Opening the file went wrong!")


value = input("enter a message: ")

try:
    if value == "" or value is None:
        raise MyError("The input is empty")
except MyError as e:
    print(e.msg)
except: 
    print("Bla")

print(value)



