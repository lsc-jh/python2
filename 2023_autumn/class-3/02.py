from random import random, randint, randrange

print(random())
print(round(random() * 1000))

print(f'Itt egy random szam 50 es 150 kozott: {randint(50, 150)}')
print(f'Itt pedig egy paros szam 100 es 200 kozott: {randrange(102, 200, 3)}')

random_numbers = []  # type: [int]

for i in range(0, 100):
    random_numbers.append(randrange(0, 10, 2))

random_numbers_2 = [randrange(0, 10, 2) for n in range(0, 100)]

print(random_numbers)
print(random_numbers_2)
