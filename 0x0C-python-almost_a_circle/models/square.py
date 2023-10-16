#!/usr/bin/python3

"""
    This module supplies the square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This class provides the blueprint
        to create a Square instance.

        It subclasses the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            This is the constructor for the
            Square class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            This method returns the width value
            of an instance of this class.
        """
        return super().width

    @size.setter
    def size(self, value):
        """
            This is the setter method of the width
            and height attribute of the Square
            instance

            It sets the width and height attributes.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            super().update(width=value, height=value)

    def __str__(self):
        """
            This method returns a string representation
            of a Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # TASK 12
    def update(self, *args, **kwargs):
        """
            This method uses non-keyworded argument
            and keyworded arguments to assign values
            to the attributes of an instance of the class
        """
        if args:
            if len(args) == 1:
                super().update(id=args[0])
            if len(args) == 2:
                super().update(id=args[0], width=args[1], height=args[1])
            if len(args) == 3:
                super().update(id=args[0], width=args[1],
                               height=args[1], x=args[2])
            if len(args) == 4:
                super().update(id=args[0], width=args[1],
                               height=args[1], x=args[2], y=args[3])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    # TASK 14
    def to_dictionary(self):
        """
            This method returns the dictionary
            representation of the class.
        """
        return self.__dict__
