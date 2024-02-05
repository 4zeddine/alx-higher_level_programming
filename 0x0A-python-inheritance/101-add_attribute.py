#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible

    Args:
        obj (any): object
        att (str): attribute name
        value (any): attribute value

    Raises:
        TypeError: if the attribute can't be added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
