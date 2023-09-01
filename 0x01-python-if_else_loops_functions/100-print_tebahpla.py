#!/usr/bin/python3
x = 0
y = 1
a = 32
i = 'z'
j = 'a'
for char in range(ord(i), ord(j) - y, - y):
    print("{}".format(chr(char - x)), end="")
    if x != 0:
        x = 0
    else:
        x = a
