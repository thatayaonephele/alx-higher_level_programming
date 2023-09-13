#!/usr/bin/python3
"""
    A module for the Student method of class type
"""


class Student:
    """
        Defines a student class
    """
    def __init__(self, first_name, last_name, age):
        """
            A function that intializes an instance of a student
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        """
            A function that retrieves a dictionary representation of student
        """
        x = self.__dict__
        return x
