#!/usr/bin/python3

"""defines a class Square."""


class Square:
    """represent a square."""

    def __init__(self, size=0):
        """initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """gets/sets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """defines the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """defines the >= compmarison to a Square."""
        return self.area() >= other.area()
