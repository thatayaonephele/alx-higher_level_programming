#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (int(x) % 3 == 0):
            print("Fizz", sep=" ")
        elif (int(x) % 5 == 0):
            print("Buzz", sep=" ")
        elif (int(x) % 15 == 0):
            print("FizzBuzz", sep=" ")
        else:
            print("{:02d}".format(x))
