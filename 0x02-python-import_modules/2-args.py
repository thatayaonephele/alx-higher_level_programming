#!/usr/bin/python3
from sys import argv


x = (len(argv)) + (-1)
if x == 1:
    print("1 argument: ")
elif x == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(x))
for y in range(x):
    print("{}: {}".format(y + 1, argv[y + 1]))
