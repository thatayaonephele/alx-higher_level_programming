#!/usr/bin/python3
"""Module defining MyClass.
"""

class MyClass:
    """Representation of MyClass.
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        # Returning a string representation of MyClass
        return f"[MyClass] {self.name} - {self.number:d}"

