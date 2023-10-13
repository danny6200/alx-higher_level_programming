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

    def to_json(self, attrs=None):
        """
            This method is used to retrieve the
            instances/objects of the student class
            in json format.

            This process is called serialization.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if key in dir(self)}

    def reload_from_json(self, json):
        """
            This method is used to convert a json
            to an object/data structure.

            This process is called deserialization
        """
        if not isinstance(json, dict):
            return

        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
