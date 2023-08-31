#!/usr/bin/python3
a = 8
b = 9
c = 10
d = 1
e = 0
for x in range(e, c):
    for y in range(x + d, c):
        if (x == a and y == b) is not True:
            print("{}{}".format(x, y), end=", ")
        else:
            print("{}{}".format(x, y))
