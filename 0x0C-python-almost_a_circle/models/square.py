#!/usr/bin/python3
"""Defines a class square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creats a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identification of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the Square.

        Args:
            *args (ints): new attribute values.
                - 1st argument represents the id attribute
                - 2nd argument represents the size attribute
                - 3rd argument represents the x attribute
                - 4th argument represents the y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for ky, val in kwargs.items():
                if ky == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif ky == "size":
                    self.size = val
                elif ky == "x":
                    self.x = val
                elif ky == "y":
                    self.y = val

    def to_dictionary(self):
        """returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
