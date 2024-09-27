#!/usr/bin/python3
"""Module representing a class named MyClass.
"""

class MyClass:
    """Class definition for MyClass with attributes.
    """

    def __init__(self, name):
        """Initialize an instance of MyClass with a name and a default number.
        
        Args:
            name (str): The name to assign to the instance.
        """
        self.name = name  # Public attribute for the name
        self.number = 0   # Public attribute for the number

    def __str__(self):
        """Return a string representation of the MyClass instance.
        
        Returns:
            str: A formatted string displaying the name and number.
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
