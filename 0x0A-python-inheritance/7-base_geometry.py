#!/usr/bin/python3

"""
    This module supplies the base geometry
    class
"""


class BaseGeometry():
    """
        This is the base geometry class

        To be improved upon in the next task
    """
    pass

    def area(self):
        """
            This function should print the area
            of a given shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            This method validates the value
            passed to the class
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than zero".format(name))
