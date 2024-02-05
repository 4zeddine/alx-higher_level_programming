#!/usr/bin/python3
"""Defines a class Square subclass of Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a Square"""
    def __init__(self, size):
        """initializes a Square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """returns an area."""
        return super().area()
