#!/usr/bin/python3
'''Module for Student class.'''


class Student:
    ''' A class that defines student'''
    def __init__(self, first_name, last_name, age):
        '''Definition of constructor method'''
        self.last_name = last_name
        self.age = age
        self.first_name = first_name

    def to_json(self, attrs=None):
        '''A function that retrieves a dictionary representation of student'''
        y = type(attrs)
        if y is list and all([type(x) != str for x in attrs]):
            return self.__dict__.copy()
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        '''A function tha loads attributes and methods from json'''
        for k, v in json.items():
            self.__dict__[k] = v
