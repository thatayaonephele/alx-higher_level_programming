#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""

    from sys import argv as av
    y = len(av)
    z = 0
    for x in range(y - 1):
        z = z + int(av[x + 1])
    print("{}".format(z))
