#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (value >= 0) is not True:
            raise ValueError('size must be >= 0')
        if (isinstance(value, int)) is not True:
            raise TypeError('size must be an integer')
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.size <= 0)is not True:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
