#!/usr/bin/python3

"""
    This module supplies the Student
    class
"""


class Student:
    """
        This is the Student class.
        It is used to create student
        object/instances.
    """
    def __init__(self, first_name, last_name, age):
        """
            This is the student's class constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            This method is used to retrieve the
            instances/objects of the student class
            in json format
        """
        return self.__dict__
