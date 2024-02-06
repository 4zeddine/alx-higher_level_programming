#!/usr/bin/python3
"""Defines a function that does text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """inserts text after each line containing a string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
