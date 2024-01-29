#!/usr/bin/python3
""" Function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints first and last name.

    Args:
        fisrt_name (str): the first name to print.
        last_name (str): the last name to print.
    Raises:
        TypeError: if either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
