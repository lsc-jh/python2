dictionary = {
    "cat": "Katze",
    "dog": "Hund",
    "horse": "Pferd",
}
phone_numbers = { 'Lucas': 123123345, 'George': 654234543 }
empty_dictionary = dict()

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary["cat"])
# print(dictionary["monkey"]) - ERROR

words = [ "cat", "lion", "horse"]

for word in words:
    if word in dictionary:
        print(f'{word} -> {dictionary[word]}')
    else:
        print(f'{word} is not in the dictionary')


animals = {
    "cat": "Katze",
    "dog": "Hund",
    "horse": "Pferd",
}

print()

print(animals.items())
for english, german in animals.items():
    print(f'{english} -> {german}')

# Kulcsokon valo vegig iteralas
for key in animals.keys():
    print(f'{key} -> {animals[key]}')

for value in animals.values():
    print(value)

# Ertek modositas

animals["cat"] = "Kätzchen"
print(animals)
animals["swan"] = "Schwan"
print(animals)
animals.update({"duck": "Ente"})
print(animals)

del animals['dog']
print(animals)
animals.popitem()
print(animals)


students = {}
while True:
    name = input("Enter the name of the turtle: ")
    if name == '':
        break
    score = int(input("Enter the age of the turtle: "))
    if name not in students:
        students[name] = (score, )
    else:
        students[name] += (score, )
print(students)
for name in sorted(students.keys()):
    add = 0
    counter = 0
    print(f'Processing: {name}, data: {students[name]}')
    for score in students[name]:
        add += score
        counter += 1
    print(f'{name}: {add / counter}')

