#!/usr/bin/python3
""" This function adds 2 integers"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Args:
        a: first number
        b: second number

    Returns:
        The sum of the numbers

    Raises:
        TypeError: if a or b are not integer and/or float numbers.

    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
