#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_num = str(number)
last_digit = string_num[-1]

msg_pt1 = "Last digit of {} is {}".format(number, last_digit)
if (int(last_digit) > 5):
    print("{} {}".format(msg_pt1, "and is greater than 5"))
if (int(last_digit) == 5):
    print("{} {}".format(msg_pt1, "and is 0"))
if ((int(last_digit) < 5 and (int(last_digit) != 0))):
    print("{} {}".format(msg_pt1, "and is less than 6 and not 0"))
