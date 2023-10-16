#!/usr/bin/python3

"""
    This module supplies the Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """
        This class is a subclass of the Base class.

        It provides the blue-print to create
        a rectangular object.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            This method is used construct an instance
            of the class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            This method returns the width value
            of an instance of this class.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            This is the setter method of the width attribute.

            It sets the width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            This is the getter method of the height attribute.

            It returns the height value of an inatance of the
            Rectangle class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            This is the setter method of the width attribute.

            It sets the height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
            This is the getter method of the x-coordinate
            attribute.

            It returns the x coordinate of an inatance of the
            Rectangle class
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            This is the setter method of the x-coordinate
            attribute.

            It sets the x coordinate of the instance of this class.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
            This is the getter method of the y-coordinate
            attribute.

            It returns the y-coordinate of an inatance of the
            Rectangle class
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            This is the setter method of the y-coordinate
            attribute.

            It sets the y-coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
            This method returns the area of a rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
            This method returns the instance of the class in string format
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            result += "\n"
        else:
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                result += " " * self.__x + "#" * self.__width + "\n"
        print(result.rstrip())

    def __str__(self):
        """
            This method overrides the default __str__
            method.
            It gives a string representation of the
            Rectangle class in the format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        id = self.id
        p_x = self.__x
        p_y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({id}) {p_x}/{p_y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """
            This method uses non-keyworded argument
            and keyworded arguments to assign values
            to the attributes of an instance of the class
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    # TASK 13
    def to_dictionary(self):
        """
            This method returns the dictionary
            representation of the class.
        """
        return self.__dict__
