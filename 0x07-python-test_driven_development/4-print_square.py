#!/usr/bin/python3
"""defines a function that prints a square"""


def print_square(size):
    """prints a square with # character.

    Args:
        size (int): size of thz square.
    Raises:
        TypeError: if size is not integer.
        ValueError: if size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        [print("#", end="") for col in range(size)]
        print("")
