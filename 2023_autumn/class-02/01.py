from visualiser.visualiser import Visualiser as vs


# Rekurziv fuggveny fontos tulajdonsagai
# 1. Fuggveny
# 2. Onnmagat meghivja
# 3. Van kilepesi feltele
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)


# Factorial
# Pelda: 5! = 5 * 4 * 3 * 2 * 1
# @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def factorial(n: int) -> int:
    if n == 1:
        return 1

    fact = factorial(n - 1)
    return n * fact


# @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# 2^3 = 2 * 2 * 2
# 4^4 = 4 * 4 * 4 * 4
# @vs(node_properties_kwargs={"shape": "record", "color": "#f57542", "style": "filled", "fillcolor": "grey"})
def power(a: int, b: int):
    if b == 0:
        return 1
    if b == 1:
        return a
    if a == 0:
        return 0

    part = power(a, b - 1)
    return a * part


def main():
    print(factorial(n=5))
    # vs.make_animation("fact.gif", delay=1000)

    print(fib(n=5))
    # vs.make_animation("fib.gif", delay=1000)

    print(power(2, 10))
    # vs.make_animation("power.gif", delay=1000)


if __name__ == "__main__":
    main()
