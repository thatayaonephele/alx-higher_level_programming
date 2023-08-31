#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "Last digit of "
y = "greater than 5"
z = "less than 6 and not 0"

if number < 0:
    x = number % (-10)
else:
    x = number % (10)
if x == 0:
    print(s + "{} is {} and is 0".format(number, x))
elif x > 5:
    print(s + "{} is {} and is {}".format(number, x, y))
else:
    print(s + "{} is {} and is {}".format(number, x, z))
