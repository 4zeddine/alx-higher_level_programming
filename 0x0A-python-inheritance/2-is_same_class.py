#!/usr/bin/python3
"""Defines a function that checks an object type"""


def is_same_class(obj, a_class):
    """function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
