#!/usr/bin/python3
"""Defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inisilizing a rectangle

        Args:
            width (int): the new Rectangle width.
            height (int): the new rectangle height.
            x (int): the new rectangle x coordinate.
            y (int): the new rectangle y coordinate.
            id (int): the new rectangle identification.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    """get/sets the width of Rictangle"""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    """get/sets the height of Rictangle"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    """get/sets the x coordinate of Rictangle"""
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    """get/sets the y coordinate of Rictangle"""
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """prints the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """returns the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the Rectangle.

        Args:
            *args (int): new attribute values.
                1st argument represents the id attribute
                2nd argument represents the width attribute
                3rd argument represent the height attribute
                4th argument represents the x attribute
                5th argument represents the y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for ky, val in kwargs.items():
                if ky == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif ky == "width":
                    self.width = val
                elif ky == "height":
                    self.height = val
                elif ky == "x":
                    self.x = val
                elif ky == "y":
                    self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
