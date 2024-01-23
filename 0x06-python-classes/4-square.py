#!/usr/bin/python3

"""defines a class Square."""


class Square:
    """represent a square."""

    def __init__(self, size=0):
        """initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/sets the size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area of the square."""
        return (self.__size * self.__size)
