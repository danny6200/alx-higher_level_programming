#!/usr/bin/python3

# TASK 1

"""
    This module supplies the base class
    which is a super class for other classes
    in the models package.
"""


import json


class Base:
    """
        This class will be the “base” of all other classes in this project. 
        The goal of it is to manage id attribute in all future
        classes and to avoid duplicating the same code. 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method is the base class constructor.
        It assigns id to public instances of the base
        class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # TASK 15
    @staticmethod
    def to_json_string(list_dictionaries):
        """
            This method converts a list of
            dictionaries to JSON string
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    # TASK 16
    @classmethod
    def save_to_file(cls, list_objs):
        """
            This method saves a list of similar
            objects to a json file
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        list_dictionaries = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as file:
            file.write(json_string)

    # TASK 17
    @staticmethod
    def from_json_string(json_string):
        """
            This method returns a list of objects
        """
        if json_string is None or json_string == "":
            return []
        
        return json.loads(json_string)

    
    # TASK 18
    @classmethod
    def create(cls, **dictionary):
        """
            This method converts a dictionary
            to an instance.
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(3, 4)
        elif cls.__name__ == "Square":
            dummy_obj = cls(5)
        
        dummy_obj.update(**dictionary)

        return dummy_obj

    #TASK 19
    @classmethod
    def load_from_file(cls):
        """
            This method returns a list
            of instances of class "cls".
        """
        class_name = cls.__name__
        filename = f"{class_name}.json"

        try:
            with open(filename, "r") as file:
                json_string = file.read()
        
        except FileNotFoundError:
            return []
        
        dictionaries = cls.from_json_string(json_string)
        
        list_obj = [cls.create(**dt) for dt in dictionaries]
        
        return list_obj
