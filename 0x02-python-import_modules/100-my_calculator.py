#!/usr/bin/python3
if __name__ == "__main__":
    """Imports all functions from calculator_1.py & handles operations."""
    from sys import argv as av, exit as e
    from calculator_1 import div, add, mul, sub
    w = len(av)
    x = 1
    y = 2
    z = 3
    if ((w - x) != z):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        e(x)
    ops = {"/": div, "+": add, "*": mul, "-": sub}
    if av[y] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        e(x)
    i = int(av[x])
    j = int(av[z])
    k = ops[av[y]](i, j)
    print("{} {} {} = {}".format(i, av[y], j, k))
