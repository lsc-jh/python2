def sum(x, y):
    return x + y


def average(x, y):
    return (x + y) / 2


def power(x, y):
    return x ** y


def prime_finder(p):
    primes = []
    for i in range(2, p):
        is_prime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                is_prime = False
                continue
        if is_prime:
            primes.append(i)
    return primes


def matrix_generator():
    my_matrix = []
    rows = int(input("How many rows do you want\n"))
    for i in range(rows):
        my_matrix.append([])
    columns = int(input("How many columns do you want\n"))
    for row in my_matrix:
        for j in range(columns):
            row.append(0)
    return myMatrix
