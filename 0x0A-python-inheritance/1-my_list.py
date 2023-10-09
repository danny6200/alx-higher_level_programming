#!/usr/bin/python3
"""
    This module supplies the MyList class.
"""


class MyList(list):
    """
        This class is a subclass of the list class.

        Attributes:
        -----------
            All atttributes in the list class
        
        Methods:
        --------
            All methods in the list class
            print_sorted (public instance method)
    """
    def __init__(self):
        """
            This constructs an instance of the MyList class
            
            It does this by accessing the super class 
            constructor method
        """
        super().__init__()

    def append(self, value):
        """
            This method allows the only integer types
            to be appended to the list
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        else:
            super().append(value)

    def print_sorted(self):
        """
            This method is specific to MyList class

            It prints the elements of the list in
            ascending order
        """
        print(sorted(self))
