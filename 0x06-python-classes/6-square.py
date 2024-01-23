#!/usr/bin/python3

"""define a class Square."""


class Square:
    """represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position)]
            [print("#", end="") for k in range(self.__size)]
            print("")
