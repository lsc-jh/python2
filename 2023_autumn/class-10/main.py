import random


def task1():
    empty_tuple = ()
    tuple1 = (1, 2, 3, 4)
    tuple2 = (1, "valami", True, [1, 2, 3], tuple1)
    print(empty_tuple, tuple1, tuple2)
    tuple3 = (1)
    print(type(tuple3))
    tuple4 = (1,)
    print(type(tuple4))
    tuple5 = 1, 10, 20
    print(tuple5)
    tuple6 = tuple((1, 2, 3))
    print(tuple6)


task1()


def task2():
    # List <-> Tuple conversion
    list1 = [1, 2, 3]
    list1.append(4)
    print(type(list1), list1)
    tuple1 = tuple(list1)
    print(type(tuple1), tuple1)
    list2 = list(tuple1)
    print(type(list2), list2)


task2()


def task3a():
    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)
    list1.append(4)
    del list1[3]
    list1.insert(1, 10)
    print(list1)

    # tuple1.append(4)
    # del tuple1[3]
    # tuple1.insert(1, 10)
    # tuple1[2] = 20
    # del tuple1


task3a()

# don't need it
# list5 = [i * (2 if i % 2 == 0 else 3) for i in range(0, 100) if i % 3 == 0]
# print(list5)

def task3b():
    list1 = [1, 2, 3, 4, 5]
    tuple1 = (1, 2, 3, 4, 5)
    print(list1[1], tuple1[1])
    print(list1[:2], tuple1[:2])
    print(list1[-3:-1], tuple1[-3:-1])
    print(len(list1), len(tuple1))


task3b()


def task4():
    tuple1 = (1, 2, 3)
    tuple2 = (1, 4, 5)
    print(tuple1 == tuple2)

    tuple3 = (3, 2, 1)
    tuple4 = (1, 2, 3)
    print(tuple3 == tuple4)

    tuple5 = (5, 5, 6)
    tuple6 = (5, 5, 6)
    print(tuple5 == tuple6)


task4()

def task5():
    tuple1 = tuple(random.randint(1, 10) for _ in range(5))
    tuple2 = tuple(random.randint(1, 10) for _ in range(5))
    print(tuple1, tuple2)
    print(tuple1 + tuple2)
    print(3 * tuple1)


task5()


def task6():
    tuple1 = tuple(random.randint(1, 10) for _ in range(5))
    print(tuple1)
    for i in tuple1:
        print(i * 3, end=" ")


task6()


def task7():
    tup1 = (1, 2, 3, 4)
    print(tup1)
    list_tup = list(tup1)
    list_tup[2] = "Lsc"
    tup1 = tuple(list_tup)
    print(tup1)
    # print(tup1[:1], "+", (33,), "+", tup1[1:])
    tup1 = tup1[:1] + (33,) + tup1[1:]
    print(tup1)
    list_tup = list(tup1)
    del list_tup[-1]
    tup1 = tuple(list_tup)
    print(tup1)


task7()

