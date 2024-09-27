#!/usr/bin/python3
# 12-student.py
"""Defines a class that models a student."""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance.
        
        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the student.
        
        If a list of attribute names is provided, only those attributes
        will be included in the dictionary.
        
        Args:
            attrs (list): (Optional) A list of attribute names to include.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
