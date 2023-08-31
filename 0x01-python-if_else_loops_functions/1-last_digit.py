#!/usr/bin/python3
from random import randint as ri
num = ri(-10000, 10000)
last_digit = abs(num) % 10
if num < 0:
    last_digit = (-1) * last_digit

msg_pt1 = "Last digit of {} is {}".format(num, last_digit)
if (int(last_digit) > 5):
    print("{} {}".format(msg_pt1, "and is greater than 5\n"), end='')
if (int(last_digit) == 5):
    print("{} {}".format(msg_pt1, "and is 0\n"), end='')
if ((int(last_digit) < 5 and (int(last_digit) != 0))):
    print("{} {}".format(msg_pt1, "and is less than 6 and not 0\n"), end='')
