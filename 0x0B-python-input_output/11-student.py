#!/usr/bin/python3
'''Module for Student class.'''


class Student:
    ''' A class that defines student'''
    def __init__(self, first_name, last_name, age):
        '''Definition of constructor method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''A function that retrieves a dictionary representation of student'''
        if attrs is None:
            return self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        '''A function that loads attributes and methods from json'''
        for k, v in json.items():
            self.__dict__[k] = v
